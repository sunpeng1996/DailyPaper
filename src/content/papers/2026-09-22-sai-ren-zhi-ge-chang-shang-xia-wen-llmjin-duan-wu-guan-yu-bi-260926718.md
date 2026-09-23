---
title: 'The Sirens'' Song: When Proximal Background Context Overshadows Distant Evidence'
title_zh: 塞壬之歌：长上下文LLM近端无关语境遮蔽远端证据的优化方案
authors:
- Xiaoyu Yang
- Jie Lu
- Wei Duan
- En Yu
affiliations:
- University of Technology Sydney
- Australian Artificial Intelligence Institute (AAII)
arxiv_id: '2609.26718'
url: https://arxiv.org/abs/2609.26718
pdf_url: https://arxiv.org/pdf/2609.26718
published: '2026-09-22'
collected: '2026-09-23'
category: LLM
direction: 长上下文LLM · 注意力机制优化
tags:
- Long-context LLM
- Attention Mechanism
- Proximity Trap
- LYRA
- ProxBench
one_liner: 提出LYRA t分布注意力匹配机制解决长上下文近端陷阱，同步发布ProxBench评测基准
practical_value: '- 电商长会话Agent、长文档商品检索场景，可直接替换最后几层注意力的QK匹配为LYRA的t分布方向匹配，无需修改整体架构，额外开销<0.04%，即可提升远端历史行为、商品信息的召回准确率

  - 长上下文RAG排序模块可借鉴LYRA的分数变换逻辑，压缩低相关文档的分数差、放大高相关文档的分数差，避免近端低相关文档抢占注意力权重

  - 可复用ProxBench的分级干扰评测思路，构建业务专属测试集，验证长会话推荐、多轮对话Agent的抗干扰能力，比如测试浏览历史、推送记录干扰下真实需求的识别准确率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有长上下文LLM优化普遍聚焦于解决距离本身带来的信息衰减，却忽略了任务无关的大量近端背景的累积竞争会抵消远端相关证据的注意力，即「近端陷阱」：即使模型能定位到远端证据，大量低相关近端内容的softmax累积权重也会遮蔽有效信号，导致远端信息利用率低，该问题在长会话推荐、多文档商品检索、多轮Agent对话等场景尤为突出。
### 方法关键点
- 提出LYRA t分布方向匹配机制，仅替换注意力的QK打分函数，保留RoPE、softmax、KV cache等原有架构完全不变：先计算RoPE变换后query和key的余弦相似度，再通过带κ参数的t分布变换重塑分数：对相似度低于阈值的低相关内容压缩分数差，对高于阈值的高相关内容放大分数差，既弱化近端低相关背景的竞争优势，又不盲目抬升所有远端内容权重。
- 发布ProxBench多粒度评测基准，分4级难度构造近端干扰测试集：固定远端证据位置，逐步提升近端背景和目标证据的语义、结构相似度，可细粒度评测模型抗近端干扰能力。
### 关键实验结果
基于Qwen3-8B仅微调最后1层Transformer块，在LongBench-v2上整体准确率达36.72%，较SOTA基线提升2.33个点；在RULER基准上8K~128K全长度段均为最优，平均准确率89.32%，较SOTA基线提升3.49个点；在ProxBench上平均准确率85.5%，较Qwen3-8B基线提升7.1个点，难度最高的L4级准确率达78%，是基线的3.4倍。
### 核心结论
长上下文信息利用的瓶颈往往不是证据距离过远，而是大量低相关近端内容的累积竞争遮蔽了有效信号，优化时优先解决近端干扰比单纯拉长上下文窗口效果更显著。
