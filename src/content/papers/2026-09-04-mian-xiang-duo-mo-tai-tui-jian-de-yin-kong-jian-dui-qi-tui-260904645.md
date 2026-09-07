---
title: Latent-Aligned Reasoning for Multimodal Recommendation
title_zh: 面向多模态推荐的隐空间对齐推理框架LARK
authors:
- Jiarui Jin
- Anyang Ji
affiliations:
- Xiaohongshu Inc.
- Nanjing University
arxiv_id: '2609.04645'
url: https://arxiv.org/abs/2609.04645
pdf_url: https://arxiv.org/pdf/2609.04645
published: '2026-09-04'
collected: '2026-09-07'
category: RecSys
direction: 多模态推荐 · VLM隐对齐推理
tags:
- Multimodal Recommendation
- VLM
- Chain-of-Thought
- Contrastive Learning
- Latent Alignment
one_liner: 提出双阶段隐对齐CoT推理框架，解决VLM多模态推荐的跨模态信号衰减问题
practical_value: '- 离线预计算的解耦架构可直接复用：LARK作为独立多模态item编码器，embedding离线预计算存储，和下游推荐模型完全解耦，无额外在线推理延迟，适配DeepFM/LightGCN等所有主流推荐架构，适合电商/内容平台大规模item库

  - 跨模态稀释的优化方案可迁移：用VLM自身冻结的视觉编码器做隐token对齐，用第一阶段CoT隐状态做第二阶段语义锚定，无需引入额外外部模型，工程实现成本低，对齐后视觉信号衰减从45%降至12%，文本从38%降至9%

  - 监督信号设计可复用：用Swing算法挖掘的item-item共现关系做对比学习的正样本，比随机负采样效果更稳定，同时大幅提升长尾冷启item的表征质量，交互<5次的长尾item
  R@20提升15%以上

  - 超参数配置可直接落地：图像patch掩码率设为50%，隐token总数16，损失权重λ_cot和λ_align设为0.1，无需大量调参即可拿到可观收益'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
VLMs应用于多模态推荐时存在跨模态稀释问题：多步推理过程中视觉、文本信号逐步衰减，传统方案要么用独立模态编码器忽略跨模态语义关联，要么直接用VLM做静态特征提取未优化推理过程，长尾冷启item的表征质量差，无法满足工业级推荐需求。
### 方法关键点
- 双阶段隐对齐推理架构：第一阶段交错插入可学习隐token和多步CoT推理，隐token与VLM自身冻结视觉编码器做patch级对齐，保留视觉感知细节；第二阶段通过Bridge MLP投影隐表征，用Swing挖掘的i2i共现信号做对比学习，中间特征与第一阶段CoT隐状态对齐，锚定推理语义
- 多损失联合优化：融合CoT生成损失（用大模型离线生成标注，无需人工标注）、视觉对齐损失、推理文本对齐损失、i2i对比损失，端到端训练
- 解耦部署：item embedding离线预计算，下游推荐模型直接调用冻结表征训练，无在线延迟
### 关键结果
在3个Amazon公开数据集和小红书1亿+MAU工业数据集上测试，对比14个SOTA基线：工业数据集上LARK+LightGCN的R@20达0.0548，比最优基线AlignRec提升10.0%；作为drop-in特征替换传统多模态特征，MMGCN等模型最高获得15.1%的R@20提升；交互<5次的长尾item上，R@20比最强基线提升15%以上。
> 最值得记住：多模态推荐中用隐空间对齐锚定VLM推理的跨模态信号，收益高于单纯扩大VLM参数规模，且落地成本更低
