package com.example.watchlistapp

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.runtime.getValue
import androidx.compose.runtime.livedata.observeAsState

// Data class for each entry in the watchlist
data class WatchListEntry(
    val id: Int,
    val name: String,
    val description: String
)

// ViewModel to provide data
class WatchListViewModel : ViewModel() {
    private val _watchList = MutableLiveData<List<WatchListEntry>>()
    val watchList: LiveData<List<WatchListEntry>> = _watchList

    init {
        // Example data
        _watchList.value = listOf(
            WatchListEntry(1, "Item 1", "Description of Item 1"),
            WatchListEntry(2, "Item 2", "Description of Item 2"),
            WatchListEntry(3, "Item 3", "Description of Item 3")
        )
    }
}

// MainActivity to set up the content
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                // Passing the ViewModel to the WatchListScreen Composable
                WatchListScreen()
            }
        }
    }
}

// Composable function to display the list of watchlist entries
@Composable
fun WatchListScreen(viewModel: WatchListViewModel = viewModel()) {
    // Observing LiveData to get the watchlist data
    val watchList by viewModel.watchList.observeAsState(emptyList())

    // LazyColumn for efficient list rendering
    LazyColumn {
        items(watchList) { entry ->
            WatchListItem(entry = entry)
        }
    }
}

// Composable function to display each entry in the list
@Composable
fun WatchListItem(entry: WatchListEntry) {
    Column(
        modifier = Modifier
            .fillMaxWidth()
            .padding(16.dp)
    ) {
        Text(text = entry.name, style = MaterialTheme.typography.headlineSmall)
        Text(text = entry.description, style = MaterialTheme.typography.bodyMedium)
    }
}

// Preview function to show a preview of the WatchListScreen
@Preview(showBackground = true)
@Composable
fun DefaultPreview() {
    MaterialTheme {
        WatchListScreen()
    }
}
