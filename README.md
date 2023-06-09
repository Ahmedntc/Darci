# D.A.R.C.I
## Image classifier discord bot

### This discord bot uses a keras model of  a neural network to predict whether an xray image of someone's chest represent that of someone that has covid or not


## Dataset

COVID-QU-Ex Dataset
......................................................................
The researchers of Qatar University have compiled the COVID-QU-Ex dataset, which consists of 33,920 chest X-ray (CXR) images including:
11,956 COVID-19
11,263 Non-COVID infections (Viral or Bacterial Pneumonia)
10,701 Normal
Ground-truth lung segmentation masks are provided for the entire dataset. This is the largest ever created lung mask dataset.
To the best of our knowledge, this is the first study that utilizes both lung and infection segmentation to detect, localize and quantify COVID-19 infection from X-ray images. Therefore, it can assist the medical doctors to better diagnose the severity of COVID-19 pneumonia and follow up the progression of the disease easily.

If you use COVID-QU-Ex Dataset in your research, please consider to cite the publications/dataset below:
[1] A. M. Tahir, M. E. H. Chowdhury, A. Khandakar, Y. Qiblawey, U. Khurshid, S. Kiranyaz, N. Ibtehaz, M. S. Rahman, S. Al-Madeed, S. Mahmud, M. Ezeddin, K. Hameed, and T. Hamid, “COVID-19 Infection Localization and Severity Grading from Chest X-ray Images”, Computers in Biology and Medicine, vol. 139, p. 105002, 2021, https://doi.org/10.1016/j.compbiomed.2021.105002.
[2] Anas M. Tahir, Muhammad E. H. Chowdhury, Yazan Qiblawey, Amith Khandakar, Tawsifur Rahman, Serkan Kiranyaz, Uzair Khurshid, Nabil Ibtehaz, Sakib Mahmud, and Maymouna Ezeddin, “COVID-QU-Ex .” Kaggle, 2021, https://doi.org/10.34740/kaggle/dsv/3122898.
[3] T. Rahman, A. Khandakar, Y. Qiblawey A. Tahir S. Kiranyaz, S. Abul Kashem, M. Islam, S. Al Maadeed, S. Zughaier, M. Khan, M. Chowdhury, "Exploring the Effect of Image Enhancement Techniques on COVID-19 Detection using Chest X-rays Images," Computers in Biology and Medicine, p. 104319, 2021, https://doi.org/10.1016/j.compbiomed.2021.104319.
[4] A. Degerli, M. Ahishali, M. Yamac, S. Kiranyaz, M. E. H. Chowdhury, K. Hameed, T. Hamid, R. Mazhar, and M. Gabbouj, "Covid-19 infection map generation and detection from chest X-ray images," Health Inf Sci Syst 9, 15 (2021), https://doi.org/10.1007/s13755-021-00146-8.
[5] M. E. H. Chowdhury, T. Rahman, A. Khandakar, R. Mazhar, M. A. Kadir, Z. B. Mahbub, K. R. Islam, M. S. Khan, A. Iqbal, N. A. Emadi, M. B. I. Reaz, M. T. Islam, "Can AI Help in Screening Viral and COVID-19 Pneumonia?," IEEE Access, vol. 8, pp. 132665-132676, 2020, https://doi.org/10.1109/ACCESS.2020.3010287.

The experiments were conducted on two CXR sets, where each set is divided into train, validation and test sets:
1) Lung Segmentation Data
Entire COVID-QU-Ex dataset (33,920 CXR images with corresponding ground-truth lung masks)
2) COVID-19 Infection Segmentation Data
A subset of COVID-QU-Ex dataset (1,456 Normal and 1,457 Non-COVID-19 CXRs with corresponding lung mask, plus 2,913 COVID-19 CXRs with
corresponding lung mask from COVID-QU-Ex dataset and corresponding infections masks from QaTaCov19 dataset).
