---
title: 'GrainSpeech: Less Context, More Detail for Compact Speech Synthesis'
title_zh: GrainSpeech：低上下文高细节的紧凑型语音合成模型
authors:
- Zitao Liang
- Chang Gao
affiliations:
- Delft University of Technology, Department of Microelectronics
arxiv_id: '2609.18856'
url: https://arxiv.org/abs/2609.18856
pdf_url: https://arxiv.org/pdf/2609.18856
published: '2026-09-16'
collected: '2026-09-17'
category: Other
direction: 边缘端紧凑型语音合成模型优化
tags:
- TinyML
- SpeechSynthesis
- EdgeDeployment
- ConvolutionalEncoder
- LossOptimization
one_liner: 用固定感受野卷积编码器与Mel专属梯度方差监督，实现仅264.8K参数的高性能边缘端语音合成
practical_value: '- 端侧电商智能硬件（如导购音箱、客服设备）的TTS部署可参考固定感受野裁剪思路，无需盲目扩大上下文窗口，大幅降低计算开销

  - 跨域损失函数迁移场景可借鉴验证-适配路径：先验证原生跨域损失的效果，再针对目标模态（如推荐的用户行为序列、多模态特征）做维度/统计特性适配

  - 资源受限场景的模型压缩可先做核心因子（如序列建模的上下文长度）的 ablation 锁定最优阈值，再针对性优化架构，避免无效调参'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
紧凑型语音声学模型长期存在质量与参数量的权衡难题，现有小参数TTS模型在内存、算力受限的边缘设备部署时生成质量不足，且编码器上下文作用、跨域监督适配两个核心瓶颈未被明确隔离验证。

### 方法关键点
1. 开展感受野缩放实验，验证自注意力上下文超过15个音素后对音高、能量、时长预测无稳定增益，据此设计固定感受野卷积编码器替代大上下文自注意力结构
2. 针对图像域梯度方差监督直接迁移到Mel谱会降低生成质量的问题，提出Mel专属梯度方差监督，包含轴专属梯度、重叠局部统计、对数域方差匹配三个优化点，保留细粒度特征的同时不损失整体质量

### 关键结果
参数量仅264.8K，不到大模型参数量的1.5%，UTMOS得分与大模型相当；在MCU上实现17.9x实时Mel谱生成，音高、能量、时长预测误差分别降低36.0%、17.3%、3.4%
