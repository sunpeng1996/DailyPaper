---
title: 'Learning from Failures: Retrieval-Centric CoT via Hard Negatives for Unified
  Multimodal Retrieval'
title_zh: 基于难例和检索中心化思维链的统一多模态检索框架UniME-R1
authors:
- Zelong Sun
- Jun Wang
- Kaicheng Yang
- Tiancheng Gu
- Ziyong Feng
- Zhiwu Lu
affiliations:
- Glint Lab
arxiv_id: '2608.06060'
url: https://arxiv.org/abs/2608.06060
pdf_url: https://arxiv.org/pdf/2608.06060
published: '2026-08-06'
collected: '2026-08-07'
category: RecSys
direction: 多模态检索 · 检索反馈式CoT优化
tags:
- Multimodal Retrieval
- Chain-of-Thought
- Hard Negative Mining
- Reinforcement Learning
- Reranking
one_liner: 提出基于检索反馈的RC-CoT多模态检索框架，自适应选择重排/重检索，复用候选索引提升效果
practical_value: '- 电商多模态搜广推场景可直接复用RC-CoT思路：基于初始召回Top-k结果反馈优化query语义，无需重建候选索引，工程落地成本极低

  - 自适应重排/重检索路由策略可迁移：根据初始召回是否包含匹配目标选择处理路径，兼顾效果与计算效率，尤其适配百万级以上大候选池场景

  - 难例挖掘+检索导向RL的训练范式可复用：用LVLM做难例判优，RL reward直接对齐最终检索指标，解决CoT生成与下游检索目标不一致的问题'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有LVLM驱动的多模态检索直接编码原始输入易丢失细粒度判别线索，无法区分语义相似的候选；主流CoT增强方法仅基于query本身生成推理，无法针对性解决检索器的实际误判问题，还可能引入冗余噪声，而全量候选生成CoT的成本极高，无法落地到大规模检索场景。
### 方法关键点
- 双组件框架：双模式Embedder先做初始召回得到Top-k候选，Adviser逐候选分析后输出结构化结果，自适应选择路径：若初始Top-k含目标直接重排，否则生成RC-CoT增强query后做全库重检索，候选仅需一次编码，索引可复用
- 检索中心化CoT（RC-CoT）：包含`<cot_focus>`（定位检索器混淆的判别特征）和`<cot_answer>`（生成面向检索的query补全），针对性修正检索方向而非泛化增强query
- 训练方案：挖掘高质量难例模拟真实检索失败场景，Adviser先做有监督微调，再用GRPO强化学习，奖励覆盖格式合规、路径判断、重排效果、CoT检索增益四个维度，全链路对齐检索目标
### 关键结果
在MMEB-V2基准上，2B参数版本比最优基线高3.1分，4B版本高1.4分；零样本下Flickr30K Recall@1达96.6，COCO达78.9，UVRB平均得分达61.6；候选编码latency比候选侧生成CoT的方案低27倍，仅增加少量query侧计算开销。
> 最值得记住的一句话：有效的检索推理不应该只解释query，更应该基于实际检索反馈诊断和修正检索器的具体误判。
