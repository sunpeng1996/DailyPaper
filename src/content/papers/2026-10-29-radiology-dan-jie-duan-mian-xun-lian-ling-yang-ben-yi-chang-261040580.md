---
title: 'RADIOlogy: A Single-Pass Approach to Training-Free Zero-Shot Anomaly Detection'
title_zh: RADIOlogy：单阶段免训练零样本异常检测方法
authors:
- Joaquín Figueira
- Giacomo D'Amicantonio
- Egor Bondarau
affiliations:
- Eindhoven University of Technology, Department of Electrical Engineering, AIMS Group
arxiv_id: '2610.40580'
url: https://arxiv.org/abs/2610.40580
pdf_url: https://arxiv.org/pdf/2610.40580
published: '2026-10-29'
collected: '2026-11-01'
category: Other
direction: 零样本异常检测 · 多模态视觉语言模型应用
tags:
- Zero-Shot Anomaly Detection
- Vision-Language Model
- Training-Free
- CLIP
- Attention Pooling
one_liner: 挖掘多模态注意力池化特性，实现免训练单阶段零样本异常检测，性能优于同类基线
practical_value: '- 电商商品瑕疵质检、二手商品成色判别场景可复用免训练检测逻辑，无需大量异常标注即可快速上线

  - 正负prompt对比打分思路可迁移到电商内容违规检测、虚假宣传图片识别等场景，降低冷启动成本

  - 单pass无滑动窗口的推理优化方法可直接复用到低延迟线上视觉检测服务，大幅降低推理耗时'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有零样本异常检测依赖复杂提示学习或高开销滑动窗口才能捕捉局部细微异常，标准CLIP的<[BOS_never_used_51bce0c785ca2f68081bfa7d91973934]> token注意力与空间块池化对局部异常特征提取能力有限，提示学习方法又需要大量辅助数据集的分割标注，医疗等垂直领域难以获取。
### 方法关键点
1. 挖掘视觉语言模型多头注意力池化的原生零样本异常定位能力，提出单阶段检测方法RADIOlogy，无需多窗口推理
2. 采用简单对比打分逻辑，计算视觉特征与正常/异常prompt集合的平均相似度判定异常
3. 结合RADIO模型的聚合特征，通过稠密异常优化pipeline增强像素级分割效果，少量修改即可适配垂直领域
### 关键结果
检测任务AUROC显著优于CLIP、WinCLIP等所有免训练基线，单张图像推理延迟仅为同类最优方法的1/10，在医疗场景适配成本极低
