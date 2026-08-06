---
title: K-EXAONE 2.0 Technical Report
title_zh: K-EXAONE 2.0 750B参数多语言开源MoE大模型技术报告
authors:
- Eunbi Choi
- Kibong Choi
- Sehyun Chun
- Seokhee Hong
- Junwon Hwang
- Hyojin Jeon
- Ahra Jo
- Hyunjik Jo
- Yeonsik Jo
- Minhyeok Jung
affiliations:
- LG AI Research
arxiv_id: '2608.04505'
url: https://arxiv.org/abs/2608.04505
pdf_url: https://arxiv.org/pdf/2608.04505
published: '2026-08-04'
collected: '2026-08-06'
category: LLM
direction: LLM 多语言MoE大模型训练优化
tags:
- MoE
- Long Context
- Speculative Decoding
- Agentic Coding
- Open LLM
one_liner: 基于上一代升级的750B总参37B激活开源MoE，支持256K上下文，代理编码与长上下文性能突出
practical_value: '- 模型升级可复用「旧模型权重上循环扩容+加随机噪声破专家对称性」的方案，大幅降低预训练成本，无需从零训练超大规模模型

  - 长上下文Agent场景可采用「保留多轮推理痕迹的Preserved Thinking模式」，解决多轮交互中推理上下文丢失问题，提升电商导购/客服Agent任务完成率

  - 大模型推理提速可直接套用DSpark+MTP双投机解码方案，FP8精度下实测端到端提速最高2.57倍，适合高并发的搜索推荐文案生成、实时Agent交互场景

  - 本地化大模型优化可参考「官方数据源+公开高价值语料」的混合数据策略，兼顾通用知识和本地文化/政策适配，适合跨境电商多语言推荐、合规内容生成场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有前沿大模型多为闭源，各国需要构建适配本地语言文化、可自主迭代的开源大模型底座；同时从零训练超大规模MoE成本极高，需要更高效的跨代模型迭代路径，兼顾性能提升与训练/推理成本控制。
### 方法关键点
- 架构：基于上一代K-EXAONE权重上循环扩容，总参从236B升至750B，激活参仅从23B升至37B，支持256K上下文，最后16层采用Clamped SwiGLU保障训练推理稳定性
- 推理优化：内置MTP+DSpark双投机解码模块，DSpark单前向生成7个token草稿块，端到端提速最高2.57倍
- 训练流程：分持续预训练、难度导向中训练、后训练三阶段，覆盖10种语言，重点强化代理编码、长上下文理解、韩国本地安全对齐能力
- Agent优化：支持Preserved Thinking模式，跨轮保留推理痕迹，提升长流程任务完成率
### 关键结果
对比上一代模型，9大类评测平均提升超10%，代理编码类指标提升约30%；长上下文检索OPENAI-MRCR从52.3分升至94.4分，256K上下文Needle-in-a-Haystack测试全位置准确率100%；韩本地安全评测ROK-FORTRESS从60.9分升至89.5分，优于同量级开源模型。
> 最值得记住的一句话：模型规模不是最终目的，通过架构迭代、训练流程优化把规模转化为可落地的实用能力，才是大模型迭代的核心目标。
