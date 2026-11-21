---
title: 'TwinD: Generalizing Deepfake Detection from Blending to Entire Face Synthesis'
title_zh: TwinD：适配融合换脸到全脸生成场景的通用深度伪造检测方法
authors:
- Andrii Yermakov
- Jan Cech
- Mario Fritz
- Jiri Matas
affiliations:
- Czech Technical University in Prague
- CISPA Helmholtz Center for Information Security
arxiv_id: '2611.25935'
url: https://arxiv.org/abs/2611.25935
pdf_url: https://arxiv.org/pdf/2611.25935
published: '2026-11-18'
collected: '2026-11-21'
category: Other
direction: 深度伪造检测 · 跨生成类型泛化
tags:
- Deepfake Detection
- AIGC Forensics
- Data Augmentation
- Model Generalization
- Image Forensics
one_liner: 提出基于两类孪生伪造样本训练的TwinD，大幅提升全脸合成深度伪造检测泛化能力
practical_value: '- 电商内容风控场景可复用孪生样本构造思路，无需依赖稀有伪造标注数据，大幅降低深度伪造检测模型的训练数据成本

  - 针对分布差异大的多类检测目标，可设计互补的专项数据增强策略，分别捕捉不同异常痕迹，提升模型跨场景泛化性

  - 风控模型冷启动阶段可仅用构造的合成样本预训练，无需真实标注伪造数据即可达到可用的检测精度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有深度伪造检测器多基于融合换脸样本训练，在无融合痕迹的全脸合成（EFS）伪造上性能骤降，最优SOTA在EFS数据集上AUROC不足78.1%，通用AIGC检测器也无法填补性能缺口。
### 方法关键点
提出TwinD检测器，基于两类自主构造的孪生伪造样本做增强训练：
1. 重建孪生：真实帧经自编码器重建后随机区域替换回真实像素，捕捉解码器生成的神经痕迹
2. 块孪生：真实帧的修改副本与原帧融合，无需生成器或人脸掩模，捕捉融合伪影
两类样本提供互补的取证线索，提升对未知伪造类型的泛化能力。
### 关键结果
在19个数据集测试集上平均AUROC达96.3%，较SOTA提升8.9个点：其中融合类数据集98.1%，EFS类数据集95.6%；仅用孪生样本训练无需深度伪造标注数据，平均AUROC也可达94.3%
