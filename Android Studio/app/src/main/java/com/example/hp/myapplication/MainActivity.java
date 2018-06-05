package com.example.hp.myapplication;

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*
import java.util.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.Layout.activity_main)

        val c = Calendae.getInstance()
        val year = c.get(Calendar.YEAR)
        val month = c.get(Calendar.MONTH)
        val day = c.get(Calendar.DAY_OF_MONTH)

        label.text = "$day/$month/$year"

        fun readData(): MutableList<ArrayModel> {
            val list = ArrayList<ArrayModel>()
            val teks  = etLokasi.text.toString()
            list.add(ArrayModel(   1,   "ITATS",  ))
            list.add
        }}
        }
