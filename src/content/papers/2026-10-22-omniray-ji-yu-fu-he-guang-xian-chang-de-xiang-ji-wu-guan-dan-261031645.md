---
title: 'OmniRay: Camera-Agnostic Monocular 3D Reconstruction with Composite Ray Fields'
title_zh: OmniRay：基于复合光线场的相机无关单目3D重建方法
authors:
- Namitha Guruprasad
- Abhay Yadav
- Cheng Peng
- Rama Chellappa
- Anand Bhattad
affiliations:
- Johns Hopkins University
- University of Virginia
arxiv_id: '2610.31645'
url: https://arxiv.org/abs/2610.31645
pdf_url: https://arxiv.org/pdf/2610.31645
published: '2026-10-22'
collected: '2026-10-24'
category: Other
direction: 相机无关单目3D重建技术
tags:
- 3D_Reconstruction
- Monocular_Vision
- Camera_Agnostic
- Ray_Field
- Neural_Rendering
one_liner: 通过分层复合光线模块实现无相机参数的跨多类型相机单目3D重建，性能达SOTA
practical_value: '- 主要为计算机视觉3D重建领域学术贡献，普通电商/搜索推荐/Agent业务可直接复用价值极低

  - 若涉及电商3D商品建模、AR试穿试戴等需从用户上传图像做3D还原的场景，可参考其无需相机参数的跨设备重建思路

  - 分层残差（基础结构+平滑残差+局部残差）的复合特征建模思路，可迁移到需兼容多分布输入的特征学习任务'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有单目3D重建模型大多默认适配针孔相机，对鱼眼、全景等广角镜头拍摄的图像重建几何失真严重；已有的相机感知模型用单一固定基表示不同相机几何，对复杂投影场景的适配性不足。
### 方法关键点
1. 提出分层复合光线场表示，将相机几何拆解为三级复杂度层级建模；
2. 光线模块由三部分组成：单调径向基捕捉径向对称结构，球谐残差捕捉平滑偏差，自由形式残差捕捉剩余局部变化，三者通过球面连续旋转组合适配任意相机几何；
3. 前馈推理无需输入相机参数，直接逐像素预测光线方向和比例径向距离，即可恢复3D点云。
### 关键结果
在针孔、GoPro、鱼眼、折反射、全景等多相机配置下实验，达到相机无关单目3D重建任务SOTA，可泛化到训练中未见过的GoPro、折反射相机配置。
