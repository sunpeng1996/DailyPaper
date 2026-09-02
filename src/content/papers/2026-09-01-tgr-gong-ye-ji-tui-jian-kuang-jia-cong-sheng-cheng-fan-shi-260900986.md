---
title: 'TGR: Advancing Industrial Recommendation from Generative-Paradigm Ranking
  toward Unified Generation and Reasoning'
title_zh: TGR：工业级推荐框架 从生成范式排序到统一生成与推理
authors:
- TGR Team
- Lei Cheng
- Haonan Hu
- Beibei Kong
- Yudong Li
- Zang Li
- Yunsheng Pang
- Hongyang Su
- Jianchao Tu
- Yunlong Wang
affiliations:
- Tencent Platform and Content Group (PCG)
arxiv_id: '2609.00986'
url: https://arxiv.org/abs/2609.00986
pdf_url: https://arxiv.org/pdf/2609.00986
published: '2026-09-01'
collected: '2026-09-02'
category: GenRec
direction: 生成式推荐 · 全栈工业落地框架
tags:
- Generative Recommendation
- Semantic ID
- Slate Generation
- LLM4Rec
- Industrial System
one_liner: 腾讯PCG推出覆盖生成式排序、端到端生成、推理增强的全栈工业生成式推荐系统，已大规模落地
practical_value: '- 排序层升级可直接复用CCFormer的降本设计：特征域分离交叉注意力+子空间token混合+层级序列压缩，训练速度比HSTU提2.21倍、单样本GFLOPs降一半，支持单批次多候选并行打分，QPS提30%

  - 端到端生成可参考两种落地路径：低侵入式NTP范式BARGE（零参数/时延上涨，获+0.6%CTR收益），或整slate生成NSP范式HiGR（P99时延<50ms，GPU需求降60%）

  - 推理增强可借鉴离线生成reason token方案，无需在请求路径执行CoT推理，冷启动新用户Hit@1提477.8%，新用户曝光转化率提13.09%

  - 全链路升级可参考渐进式路径：先替换排序层（GenRank），再迭代端到端生成（GenRec），最后叠加推理增强，避免一次性替换的业务风险'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统级联推荐系统存在三大结构性痛点：1）碎片化DLRM架构无LLM式缩放定律，模型容量、算力增加后效果快速饱和；2）分阶段优化、逐点item打分忽略item间依赖和位置效应，整slate推荐质量受损；3）ID式共驱模型缺乏多模态语义、世界知识和推理能力，冷启动、长尾、模糊意图场景表现差，工业界迫切需要可落地、低侵入的生成式推荐全栈方案。

### 方法关键点
- 三层模块化架构，支持渐进式落地：1）TGR-GenRank：CCFormer作为drop-in排序替换，采用特征域分离交叉注意力、长序列子空间token混合、层级序列压缩优化，保留逐item多任务打分能力适配现有链路；2）TGR-GenRec：支持两种生成范式，NTP范式BARGE通过item上下文感知注意力、层级路径重排序、正交双路解码解决多token item边界丢失和语义漂移问题；NSP范式HiGR通过前缀结构化Semantic ID、粗到细整slate解码器、列表级多目标对齐，直接生成整页推荐结果；3）TGR-Reason：离线训练Think模型生成reason token，在线注入解码过程，无请求时推理开销。

### 关键结果
全栈已落地腾讯新闻、视频、网文等场景，服务数亿用户：CCFormer在视频推荐场景CTR+3.57%，广告排序场景广告收入+1.71%；BARGE作为生成式召回通道，Hit@5相对OneRec提10.2~16.9%，CTR+0.6%，总阅读时长+1.7%；HiGR整slate生成P99<50ms，GPU需求比全序列解码降60%，平均观看时长+1.22%，广告收入+0.56%；Reason模块冷启动新用户Hit@1+477.8%，新用户曝光转化率+13.09%。

最值得记住的一句话：生成式推荐落地不需要一次性替换全链路，可通过渐进式升级、分范式适配业务时延要求，在不增加资源预算的前提下拿到稳定业务收益。
