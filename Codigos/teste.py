import numpy as np
import cv2
import matplotlib.pyplot as plt

# img1 = cv2.imread('box.png',cv2.IMREAD_GRAYSCALE) # queryImage
# img2 = cv2.imread('box_in_scene.png',cv2.IMREAD_GRAYSCALE) # trainImage
# 
# sift = cv2.SIFT_create()
# 
# kp1, des1 = sift.detectAndCompute(img1,None)
# kp2, des2 = sift.detectAndCompute(img2,None)
# 
# FLANN_INDEX_KDTREE = 1
# index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
# search_params = dict(checks=50) # or pass empty dictionary
# flann = cv2.FlannBasedMatcher(index_params,search_params)
# matches = flann.knnMatch(des1,des2,k=2)
# 
# matchesMask = [[0,0] for i in range(len(matches))]
# 
# for i,(m,n) in enumerate(matches):
#     if m.distance < 0.7*n.distance:
#         matchesMask[i]=[1,0]
#     
# draw_params = dict(matchColor = (0,255,0), singlePointColor = (255,0,0), matchesMask = matchesMask, flags = cv2.DrawMatchesFlags_DEFAULT)
# img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
# 
# plt.imshow(img3,),plt.show()

def main():
    webcam = cv2.VideoCapture(0)
    
    while True:
        validacao, frame = webcam.read()
    
        if validacao:           
            img1 = cv2.imread(frame, cv2.IMREAD_GRAYSCALE) 
            img2 = cv2.imread('C:\CODE\PraticaBasica\Python\OpenCV\Meus_code\Foto_frame.png', cv2.IMREAD_GRAYSCALE) 

            sift = cv2.SIFT_create()
            
            kp1, des1 = sift.detectAndCompute(img1,None)
            kp2, des2 = sift.detectAndCompute(img2,None)
            
            FLANN_INDEX_KDTREE = 1
            index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
            search_params = dict(checks=50) # or pass empty dictionary
            flann = cv2.FlannBasedMatcher(index_params,search_params)
            matches = flann.knnMatch(des1,des2,k=2)
            
            matchesMask = [[0,0] for i in range(len(matches))]
            
            for i,(m,n) in enumerate(matches):
                if m.distance < 0.7*n.distance:
                    matchesMask[i]=[1,0]
                
            draw_params = dict(matchColor = (0,255,0), singlePointColor = (255,0,0), matchesMask = matchesMask, flags = cv2.DrawMatchesFlags_DEFAULT)
            img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
            
            plt.imshow(img3,),plt.show()
            
            if cv2.waitKey(1) != -1:
                break
        else:
            break    
    webcam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()