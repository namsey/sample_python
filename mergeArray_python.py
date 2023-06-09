using System;
using System.IO;

class MainClass
{
    public static void Main(string[] args)
    {
        try
        {
            // Creates a FileStream
            FileStream file = new FileStream("input.txt", FileMode.Open);

            // Creates a BufferedStream
            BufferedStream input = new BufferedStream(file);

            // Reads first byte from file
            int i = input.ReadByte();

            while (i != -1)
            {
                Console.Write((char)i);

                // Reads next byte from the file
                i = input.ReadByte();
            }

            input.Close();
        }
        catch (Exception e)
        {
            Console.WriteLine(e.StackTrace);
        }
    }
}
