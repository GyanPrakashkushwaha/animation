using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Linq;
using System.Threading;

public class animeCode : MonoBehaviour
{
    public GameObject[] Body;
    List<string> lines;
    int counter = 0;


    void Start()
    {
        lines = System.IO.File.ReadLines("Assets/points.txt").ToList();
    }

    // Update is called once per frame
    void Update()
    {
        // print(lines[0]);
        string[] point = lines[counter].Split(',');
        // convert the string values to float. And also divide all those into x,y and z
        for(int i =0; i <=32;i++){
            float x = float.Parse(point[0+(i*3)])/50;
            float y = float.Parse(point[1+(i*3)])/50;
            float z = float.Parse(point[2+(i*3)])/50;
            Body[i].transform.localPosition = new Vector3(x,y,z);
        }
        
        counter +=1;
        if (counter == lines.Count) {
            counter = 0;
        }
        Thread.Sleep(30);
    }
}
