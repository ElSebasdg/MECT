LIBRARY ieee;
USE ieee.STD_LOGIC_1164.ALL;
USE ieee.STD_LOGIC_ARITH.ALL;
USE ieee.STD_LOGIC_UNSIGNED.ALL;

LIBRARY logic;
USE logic.ALL;

entity parallelEncoder is
    Port (
        word : in  STD_LOGIC_VECTOR(15 downto 0);
        crc_out  : out STD_LOGIC_VECTOR(7 downto 0)
    );
end parallelEncoder;

ARCHITECTURE behave OF parallelEncoder IS
	COMPONENT XOR_6
        PORT(
            A : IN std_logic;
            B : IN std_logic;
            C : IN std_logic;
            D : IN std_logic;
            E : IN std_logic;
            F : IN std_logic;
            G : IN std_logic;
            Y : OUT std_logic
        );
    END COMPONENT;

    COMPONENT XOR_7
        PORT(
            A : IN std_logic;
            B : IN std_logic;
            C : IN std_logic;
            D : IN std_logic;
            E : IN std_logic;
            F : IN std_logic;
            G : IN std_logic;
            H : IN std_logic;
            Y : OUT std_logic
        );
    END COMPONENT;

    COMPONENT XOR_9
        PORT(
            A : IN std_logic;
            B : IN std_logic;
            C : IN std_logic;
            D : IN std_logic;
            E : IN std_logic;
            F : IN std_logic;
            G : IN std_logic;
            H : IN std_logic;
            I : IN std_logic;
            J : IN std_logic;
            Y : OUT std_logic
        );
    END COMPONENT;


    signal temp_out0, temp_out1, temp_out2, temp_out3, temp_out4, temp_out5, temp_out6, temp_out7: STD_LOGIC;
begin 
     -- 7
    -- temp_out0 <= XOR_7(word(0), word(1), word(2), word(4), word(6), word(8), word(13), word(14));
    XOR_7_inst : XOR_7
    port map (
        A => word(0),
        B => word(1),
        C => word(2),
        D => word(4),
        E => word(6),
        F => word(8),
        G => word(13),
        H => word(14),
        Y => temp_out0
    );

	 -- 9
    -- temp_out1 <= XOR_9(word(0), word(3), word(4), word(5), word(6), word(7), word(8), word(9), word(13), word(15));
    XOR_9_inst1 : XOR_9
    port map (
        A => word(0),
        B => word(3),
        C => word(4),
        D => word(5),
        E => word(6),
        F => word(7),
        G => word(8),
        H => word(9),
		  I => word(13),
		  J => word(15),
        Y => temp_out1
    );
	 
	 -- 6
    -- temp_out2 <= XOR_6(word(0), word(2), word(5), word(7), word(9), word(10), word(13));
	 XOR_6_inst1 : XOR_6
    port map (
        A => word(0),
        B => word(2),
        C => word(5),
        D => word(7),
        E => word(9),
        F => word(10),
        G => word(13),
        Y => temp_out2
    );
	 
	-- 6
	-- temp_out3 <= XOR_6(word(1), word(3), word(6), word(8), word(10), word(11), word(14));
	XOR_6_inst2 : XOR_6
		 port map (
			  A => word(1),
			  B => word(3),
			  C => word(6),
			  D => word(8),
			  E => word(10),
			  F => word(11),
			  G => word(14),
			  Y => temp_out3
		 );
		 
	-- 6
   -- temp_out4 <= XOR_6(word(2), word(4), word(7), word(9), word(11), word(12), word(15));
	XOR_6_inst3 : XOR_6
		 port map (
			  A => word(0),
			  B => word(1),
			  C => word(3),
			  D => word(5),
			  E => word(7),
			  F => word(12),
			  G => word(13),
			  Y => temp_out4
		 );
		 
	 -- 9
    -- temp_out5 <= XOR_9(word(0), word(1), word(2), word(3), word(4), word(5), word(6), word(10), word(12), word(14));
	 XOR_9_inst2 : XOR_9
    port map (
        A => word(0),
        B => word(1),
        C => word(2),
        D => word(3),
        E => word(4),
        F => word(5),
        G => word(6),
        H => word(10),
		  I => word(12),
		  J => word(14),
        Y => temp_out5
    );
	 
	 -- 9
    -- temp_out6 <= XOR_9(word(1), word(2), word(3), word(4), word(5), word(6), word(7), word(11), word(13), word(15));
	 XOR_9_inst3 : XOR_9
    port map (
        A => word(1),
        B => word(2),
        C => word(3),
        D => word(4),
        E => word(5),
        F => word(6),
        G => word(7),
        H => word(11),
		  I => word(13),
		  J => word(15),
        Y => temp_out6
    );
		
	 -- 6
    -- temp_out7 <= XOR_6(word(0), word(1), word(3), word(5), word(7), word(12), word(13));
	
	 XOR_6_inst4 : XOR_6
    port map (
        A => word(0),
        B => word(1),
        C => word(3),
        D => word(5),
        E => word(7),
        F => word(12),
        G => word(13),
        Y => temp_out7
    );
	 
    -- Assign outputs
    crc_out(0) <= temp_out0;
    crc_out(1) <= temp_out1;
    crc_out(2) <= temp_out2;
	 crc_out(3) <= temp_out3;
	 
	 crc_out(4) <= temp_out4;
    crc_out(5) <= temp_out5;
    crc_out(6) <= temp_out6;
	 crc_out(7) <= temp_out7;
    
end behave;

	 
	 
