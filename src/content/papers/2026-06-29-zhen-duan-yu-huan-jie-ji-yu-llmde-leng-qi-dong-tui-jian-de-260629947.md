---
title: Diagnosing and Mitigating Retrieval Bottlenecks in LLM-Based Cold-Start Recommendation
title_zh: 诊断与缓解基于LLM的冷启动推荐中的检索瓶颈
authors:
- Zhe Dong
- Fang Qin
- Manish Shah
- Yicheng Wang
affiliations:
- University of Maine at Presque Isle
- Stanford University
- Independent Researcher
arxiv_id: '2606.29947'
url: https://arxiv.org/abs/2606.29947
pdf_url: https://arxiv.org/pdf/2606.29947
published: '2026-06-29'
collected: '2026-06-30'
category: RecSys
direction: LLM冷启动推荐 · 检索瓶颈诊断
tags:
- LLM4Rec
- cold-start
- multi-retriever
- hybrid-fusion
- retrieval
one_liner: 拆分检索与重排评价，揭示LLM冷启动推荐瓶颈在检索覆盖率，提出LHF融合方法
practical_value: '- 冷启动/新商品推荐场景，优先优化检索覆盖率，不要把大量计算资源投在在线prompt式LLM重排，性价比极低

  - 多检索源融合可复用LHF方案：取多检索器的候选并集，在验证集训练轻量GBDT，融入item-new、用户冷度等元特征，效果优于启发式RRF等融合方法

  - 针对新商品曝光需求，可通过对LHF训练中的item-new样本做加权，提升新品覆盖率，仅牺牲少量热门商品效果

  - LLM的语义能力建议用在离线item表征生成、检索监督阶段，而非在线重排环节'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于LLM的推荐普遍采用检索后LLM重排的pipeline，默认LLM的语义理解能解决冷启动问题，但多数研究评测时会将目标商品注入候选池，掩盖了检索环节的真实瓶颈，无法反映新商品冷启动场景的真实效果，因此需要拆分检索覆盖率和重排质量做独立诊断。

### 方法关键点
- 设计三阶段评估协议：①正控制池（注入目标商品，隔离评测重排质量）②检索真实池（不注入目标，直接评测检索覆盖率）③端到端全流程评测，将端到端召回分解为`覆盖率 × 条件重排召回`
- 提出LHF（Learned Hybrid Fusion）：取多检索器输出的top候选并集，提取检索排名/命中标记、item-new标记、用户冷度、item文本长度等serving可用特征，仅用验证集训练GBDT重排输出top-N候选，无数据泄漏
- 构建五个领域的时间拆分冷启动基准，符合真实业务的时序分隔要求

### 关键结果
- 正控制重排：Qwen3从8B放大到32B仅缩小和强协同基线的差距，仅在文本丰富的MIND域超过基线，其余四域仍落后
- 真实检索：标准单检索器top200覆盖率仅4.6%~22.9%，核心原因是32%~91%的冷启动目标是训练无交互的全新商品；LHF将覆盖率提升到6.1%~24.3%，内容丰富域可拿到oracle提升空间的17%~61%
- 端到端：LHF优化后的候选池，轻量LightGBM重排效果远好于prompt式LLM重排，LLM重排反而降召回；Qwen3-8B吞吐量仅为LightGCN的1/1000，性价比极低

### 核心结论
LLM冷启动推荐的可落地收益在检索环节，不在在线prompt重排阶段
