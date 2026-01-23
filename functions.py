 def prediction_to_answer(prediction, treshold=0.5):
-    pass
\ No newline at end of file
+    if prediction <= treshold:
+       return "yes"
+    else:
+       return "no"
\ No newline at end of file 
