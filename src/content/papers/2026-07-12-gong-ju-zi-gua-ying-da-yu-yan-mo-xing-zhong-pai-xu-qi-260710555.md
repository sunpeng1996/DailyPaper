---
title: Tool-Adaptive LLM Reranker
title_zh: 工具自适应大语言模型重排序器TALRanker
authors:
- Zichuan Liu
- Ruijin Hua
affiliations:
- Carnegie Mellon University
- Huazhong University of Science and Technology
arxiv_id: '2607.10555'
url: https://arxiv.org/abs/2607.10555
pdf_url: https://arxiv.org/pdf/2607.10555
published: '2026-07-12'
collected: '2026-07-14'
category: RecSys
direction: LLM增强重排序 · 智能体工具调用
tags:
- Reranker
- LLM
- Agent
- Tool Calling
- Reinforcement Learning
- Information Retrieval
one_liner: 将点式重排序建模为智能体MDP，自适应调用工具平衡重排序精度与推理效率
practical_value: '- 微调LLM重排序器时可直接复用「混合loss设计」：仅在最终打分token计算BCE损失，其余所有token加KL散度对齐基座，既保证打分能力，又保留基座的工具调用、推理能力，避免灾难性遗忘

  - 成本感知的不对称RL奖励可直接迁移到工具调用类任务：未调用工具且答错给重罚、调用工具给固定小额惩罚、答对无工具调用给最高奖励，迫使模型自主判断工具调用时机，平衡精度和延迟

  - 工程上可复用自适应路由架构：将重排序流程改造为MDP，解码时拦截<tool_call>特殊token触发外部检索，结果拼回上下文后继续推理，适合电商搜索长尾专业query、参数类query的重排序场景

  - 业务选型参考：4B参数量的TALRanker效果超过14B纯参数重排序器，小模型加自适应工具调用的性价比远高于盲目堆参数量，可大幅降低部署成本'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM重排序器受参数知识边界限制，处理长尾、知识密集型query时容易出现事实幻觉，全量调用外部检索工具又会导致推理延迟过高，无法满足工业级搜索推荐的 latency 要求，此前方案始终无法在精度和效率间取得最优平衡。
### 方法关键点
- 将点式重排序建模为智能体MDP：模型输出<answer>特殊token时直接输出相关性分数，输出<tool_call>时触发外部检索，检索结果拼回上下文后继续推理，实现动态路由
- 两阶段训练范式：第一阶段warmup采用混合损失，仅在最终yes/no打分token计算BCE损失，其余所有token用KL散度对齐基座模型分布，避免灾难性遗忘，保留基座的推理和工具调用能力；第二阶段采用GRPO强化学习，设计不对称成本感知奖励，包括格式合规奖励、工具调用次数惩罚、不对称精度奖励（未调用工具且答错罚-1，调用工具答错罚0，答对按误差给正向奖励）
### 关键结果
在TREC-DL、BEIR、BRIGHT三类基准上测试，对比Rank1、Rank-R1、REARANK等SOTA基线：8B版本TALRanker在BEIR基准平均NDCG@10达46.3，超过14B参数的Rank-R1 2.5个点；在推理密集型BRIGHT基准NDCG@10达29.7，较SOTA提升3.3个点；单GPU吞吐量达778 queries/hour，和纯参数点式重排序器持平，工具调用率仅0.28%以下。
### 核心结论
给重排序模型增加自适应工具调用能力，比盲目扩大模型参数量的性价比高得多。
