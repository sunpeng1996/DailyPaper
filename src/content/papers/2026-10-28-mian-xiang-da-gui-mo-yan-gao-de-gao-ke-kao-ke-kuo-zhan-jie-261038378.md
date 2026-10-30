---
title: Towards Reliable, Scalable, and Value-Aligned Generative Recommendation for
  Large-Scale Advertising
title_zh: 面向大规模广告的高可靠、可扩展、价值对齐生成式推荐
authors:
- Yatong Xiao
- Yibo Sheng
- Lixiang Wang
- Mingjie Sun
- Yunhao Sha
- Pengfei Zhang
- Shengyu Wang
- Peng Wang
- Wenjin Wu
- Peng Jiang
affiliations:
- Kuaishou Technology
arxiv_id: '2610.38378'
url: https://arxiv.org/abs/2610.38378
pdf_url: https://arxiv.org/pdf/2610.38378
published: '2026-10-28'
collected: '2026-10-30'
category: GenRec
direction: 生成式推荐 · 工业广告系统落地优化
tags:
- Generative Recommendation
- Semantic ID
- Value Alignment
- Advertising
- Model Scaling
one_liner: 快手提出GR4AD-X生成式广告推荐框架，严格时延约束下收入较基线涨3.07%
practical_value: '- SID构造可复用Multi-Path方案：给语义边界item多分配m组首阶聚类SID，无需提升解码深度即可提升召回率，快手实验显示首阶Hit@1相对涨22%，收入涨0.58%

  - 模型扩缩避免盲目堆参：沿输入信号、编码器、词表内存、残支流、决策深度5个维度互补扩容，同0.5B参数规模下，收入涨幅是纯堆参的2.66倍，QPS是2.57倍

  - 全链路价值对齐可复用UniVGD框架：训练阶段做前缀级eCPM奖励传播、推理阶段用RRF融合生成概率与前缀价值做剪枝、生成后复用同一模型加判别头重排，收入额外涨1.07%'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
已落地的工业生成式广告推荐框架GR4AD暴露三个核心问题：确定性SID分配对语义边界敏感，边界广告易被早剪枝；纯堆backbone参数边际收益递减，0.5B参数较0.16B仅多涨0.53%收入但QPS下降67%；序列级价值优化对中间SID决策的credit分配不足，生成概率排序与eCPM排序的HitRate@10仅0.02，高价值候选易被提前淘汰。

### 方法关键点
- 可靠SID构造：Multi-Path SID给每个广告保留top-m个首阶聚类结果，每个分支独立做剩余量化，多路径联合训练，推理时广告级去重，不增加解码深度
- 高效扩缩策略：沿5个互补维度扩容：输入新增20+用户/上下文特征、编码器升级SwiGLU FFN、引入分层前缀门控内存PCGM扩词表、增加4路对角超连接残支流、新增推理前缀token提升首阶决策准确率
- 全链路价值对齐UniVGD：训练时自底向上传播eCPM奖励到每个SID前缀做PV-RSPO优化；推理时用RRF融合生成概率与前缀价值做beam剪枝；生成后复用同一模型加判别头做eCPM和转化目标重排

### 关键实验
在快手4亿+用户的广告系统做在线A/B测试，基线为已落地的GR4AD：全量GR4AD-X累计收入提升3.07%；其中Multi-Path SID单独提0.58%，多维度扩缩累计提1.42%，UniVGD累计提1.07%；高eCPM广告的HitRate@10从0.02提升到0.3，同参数规模下比纯堆参方案QPS高157%，收入涨幅高166%。

### 最值得记住的话
工业生成式推荐优化不要盲目堆大模型参数，从表示可靠性、多维度高效扩缩、全链路业务价值对齐三个方向优化，能在严格时延约束下获得更高的业务收益。
