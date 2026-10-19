---
title: Reasoning Reranking with Semantic IDs as the Sole Item Representation
title_zh: 仅使用Semantic ID作为物品表示的推理式重排序研究
authors:
- Zhenwei Tang
- Jintao Liu
- Di Bai
- Xidong Wu
- Xinwu Cheng
affiliations:
- Google
- University of Toronto
arxiv_id: '2610.22797'
url: https://arxiv.org/abs/2610.22797
pdf_url: https://arxiv.org/pdf/2610.22797
published: '2026-10-16'
collected: '2026-10-19'
category: GenRec
direction: 生成式推荐 · Semantic ID推理重排序
tags:
- Semantic ID
- Reranking
- LLM4Rec
- SFT
- RLVR
- LoRA
one_liner: 验证仅用Semantic ID做推理重排序的可行性，效果媲美使用20倍长文本prompt的通用LLM
practical_value: '- 长用户历史场景可优先用SID做重排序：SID prompt比文本短20~28倍，避免长文本上下文超限、性能衰减问题，大幅降低推理成本

  - 后训练Pipeline可直接复用：先用SFT消除输出格式错误（返回输入顺序、推理循环），8B及以上规模模型再加分级NDCG奖励的RLVR微调，效果优于二元Hit@1奖励

  - 工业落地可采用混合方案：用SID完成全候选集重排序，再召回Top N物品的元数据生成解释文案，兼顾重排序效率与可解释性的准确性'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前生成式推荐普遍采用Semantic ID（SID）表示物品，不仅能大幅缩短prompt长度，其嵌入还融合了用户行为的协同信号，比纯文本信息包含更多偏好特征；但现有推理式重排序系统都依赖物品文本元数据，仅用SID能否完成推理重排序的能力未被验证，且原生SID预训练模型普遍存在输出格式错误（直接返回输入顺序、推理循环）等问题，无法直接落地。

### 方法关键点
- 搭建RERANKID可控测试床，支持仅SID、仅文本、混合三种物品渲染方式，可单变量控制历史长度、候选集规模，同时统计输出格式错误率
- 对比4种后训练方案：SFT（模仿文本视角的教师标注轨迹）、OPD（基于学生采样轨迹的同策略蒸馏）、RFT（拒绝采样自训练）、RLVR（基于分级排序奖励的强化学习），所有方案均用LoRA微调，不改动SID嵌入
- 对比分级NDCG@5奖励与二元Hit@1奖励的效果差异，验证奖励设计的影响

### 关键结果
基于快手短视频数据集、OpenOneRec 1.7B/8B预训练模型实验，对比Gemini-3.6等通用LLM基线：
- 8B模型经SFT+RLVR（分级NDCG奖励）微调后，仅用845token的SID prompt，NDCG@5达0.277，和使用16722token（20倍长）文本prompt的Gemini-3.6效果相当
- 无用户历史时，该模型仅靠候选SID就能显著超过随机排序，而文本基线Gemini-3.6表现与随机无差异
- 历史长度达256时，文本基线prompt超50k token效果下降，SID模型仍保持性能稳定

### 最值得记住的一句话
纯SID推理重排序可兼顾效率与效果，当前标准后训练能让模型学会排序但无法生成准确的物品描述，落地需结合元数据做解释
