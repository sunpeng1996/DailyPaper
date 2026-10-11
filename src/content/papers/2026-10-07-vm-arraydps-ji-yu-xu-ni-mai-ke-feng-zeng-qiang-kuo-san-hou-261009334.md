---
title: 'VM-ARRAYDPS: Virtual Microphone Augmented Diffusion Posterior Sampling for
  Unsupervised Blind Speech Separation'
title_zh: VM-ARRAYDPS：基于虚拟麦克风增强扩散后验采样的无监督盲语音分离
authors:
- Jingqi Sun
- Haozhan Tang
- Shulin He
- Zhong-Qiu Wang
affiliations:
- Department of Computer Science and Engineering, Southern University of Science and
  Technology
arxiv_id: '2610.09334'
url: https://arxiv.org/abs/2610.09334
pdf_url: https://arxiv.org/pdf/2610.09334
published: '2026-10-07'
collected: '2026-10-11'
category: Other
direction: 无监督盲语音分离 · 扩散模型应用
tags:
- Blind Speech Separation
- Diffusion Model
- Posterior Sampling
- Virtual Microphone
- Multi-channel Consistency
one_liner: 通过IVA生成高信噪比虚拟麦克风补充多通道一致性约束，提升少麦克风场景盲语音分离性能
practical_value: '- 虚拟观测增强思路可迁移至多模态内容理解/召回场景：当物理观测（如用户行为、内容特征）稀疏低质时，可通过统计先验生成高置信度虚拟样本补充约束，提升建模效果

  - 多源异质约束加权融合技巧可复用：如RAG生成、GenRec结果校准场景，可对不同置信度的约束（业务规则、用户历史、召回结果）加权纳入生成目标，减少幻觉

  - 传统统计方法+大模型生成先验的融合范式，可解决冷启动场景标注数据不足的问题，比如新品推荐、新用户画像建模'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
盲语音分离（BSS）中基于扩散模型的ArrayDPS方法依赖多通道一致性（MC）约束引导后验采样，当物理麦克风数量少、采集信号信噪比低时，约束有效性大幅下降，模型性能受限。
### 方法关键点
1. 采用传统独立向量分析（IVA）对物理麦克风观测做空间解混，生成高信噪比的虚拟麦克风观测
2. 设计加权多通道一致性目标，同时纳入物理+虚拟麦克风信号，引导扩散后验采样过程优化源信号恢复
3. 全程为无监督范式，无需配对的混合-纯净源训练数据
### 关键结果
在混响场景的2说话人、3说话人分离任务上，性能显著优于基线ArrayDPS；消融实验验证了虚拟麦克风数量、虚拟MC约束权重对分离效果的影响规律。
