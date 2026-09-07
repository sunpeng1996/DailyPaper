---
title: Adaptive Gated Deepfake Detection for Low-Resolution and Resource-Constrained
  Environments
title_zh: 面向低分辨率资源受限场景的自适应门控深度伪造检测
authors:
- Vaishnavi Sen
- Cody Laurie
- Rashida Hasan
affiliations:
- California State University, Northridge
arxiv_id: '2609.05320'
url: https://arxiv.org/abs/2609.05320
pdf_url: https://arxiv.org/pdf/2609.05320
published: '2026-09-04'
collected: '2026-09-07'
category: Other
direction: 低资源场景·自适应推理·深度伪造检测
tags:
- DeepfakeDetection
- AdaptiveInference
- MultiExitArchitecture
- LowResource
- DynamicRouting
one_liner: 提出图像质量驱动路由的多出口深度伪造检测框架，平衡精度与推理效率
practical_value: '- 电商内容审核场景下的生成式虚假图片（如AI生成商品图、伪造人脸评价）检测可直接复用该自适应门控架构，降低边缘端/低算力服务器的推理成本

  - 资源受限的推理服务可参考多出口动态路由思路：根据输入质量（如图像分辨率、query清晰度）给简单样本分配更短的推理路径，平均延迟可大幅降低

  - 分类任务中引入输入质量感知的gate模块，可在不损失整体精度的前提下大幅提升高质量样本的推理速度，适配推荐/广告的实时性要求'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有深度伪造检测模型依赖高质量输入、固定推理路径、算力开销大，无法适配低分辨率、资源受限的落地场景，且在类别不平衡数据下性能衰减明显。
### 方法关键点
提出AdaGate-DF自适应门控检测框架，引入图像质量感知路由机制，搭配双路径多出口架构，高质量简单样本可提前退出推理，大幅降低不必要的算力消耗，同时支持不确定性感知预测。
### 关键结果数字
在Celeb-DF数据集上AUC达0.9370，优于MaD-CoRN、DefakeHop++等基线，同时保持低推理延迟；384×384分辨率下AUC可达0.9708；在FaceForensics++数据集的类别不平衡场景下性能仍具备竞争力，实现精度、不确定性感知、计算效率三者平衡。
