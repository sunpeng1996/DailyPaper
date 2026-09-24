---
title: 'Risk-Controlled KV-Cache Eviction: From Memory Budgets to Risk Targets'
title_zh: 风险可控的KV缓存驱逐：从内存预算导向转向风险目标导向
authors:
- Beomgu Kang
- SoJin Yun
- Hojoon Kim
- Hyunseok Seo
affiliations:
- Department of Artificial Intelligence, Korea University
arxiv_id: '2609.27981'
url: https://arxiv.org/abs/2609.27981
pdf_url: https://arxiv.org/pdf/2609.27981
published: '2026-09-23'
collected: '2026-09-24'
category: LLM
direction: LLM推理优化 · KV cache风险控制
tags:
- KV-cache
- Risk-Control
- LLM-Inference
- Learn-then-Test
- Long-Context
one_liner: 提出压缩器无关的校准框架，实现KV缓存驱逐的有限样本风险控制
practical_value: '- 部署LLM电商导购、推荐文案生成、长会话Agent服务时，可复用该框架：先定义业务可接受的效果下降阈值（如推荐点击率下降容忍度、问答准确率下降容忍度）和超标概率，再通过校准数据选择最优KV压缩策略，兼顾内存成本和业务效果稳定性

  - 针对长上下文任务（如用户长行为序列召回、多商品资料问答），不要仅依赖平均效果选KV缓存策略，需额外控制长尾请求的效果劣化概率，避免小部分用户体验受损

  - 混合任务LLM服务可采用任务分层校准设计，对不同任务分别设置风险阈值，避免整体平均风险达标但单任务劣化严重的问题

  - 上线前可参考有限样本检验逻辑，避免仅靠离线经验阈值选策略导致线上风险超标的问题'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有KV缓存驱逐策略仅聚焦平均效果与内存的权衡，较小的平均效果损失可能掩盖单请求的大幅劣化，无法保障工业级部署的可靠性。长上下文LLM服务（如多文档问答、长会话Agent）对单请求效果稳定性要求高，需直接控制效果劣化的超标概率，而非仅依据平均表现分配内存预算。
### 方法关键点
- 将KV缓存驱逐重构为风险控制问题：定义相对全缓存推理的效果下降超过业务容忍阈值τ为劣化事件，部署风险为劣化事件的群体发生概率，要求风险不超过设定上限ϵ，且提供有限样本保证（校准抽样下风险超标的概率≤δ）
- 基于Learn-then-Test框架实现压缩器无关的校准流程：无需修改底层KV驱逐算法，将候选策略按保守到激进排序，用独立校准集依次检验，返回首个通过检验的最激进策略，无合格策略时自动回退全缓存模式
- 支持固定预算、请求自适应两类KV策略，采用任务分层采样校准，保障任务均衡分布下的风险控制有效性
### 关键结果
在(τ=0.1, ϵ=0.05, δ=0.05)的通用可靠性合约下：
- LongBench测试集中，Llama-3.1-8B的Layer-DefensiveKV可在35%缓存保留率下实现4%的实测劣化风险，比经验阈值选择的策略保留率高5~10个百分点，避免了隐性风险
- RULER-32K测试集中，SnapKV无合格压缩策略，自动回退全缓存，满足风险要求
### 核心结论
仅用平均效果衡量KV缓存优化效果存在显著缺陷，工业部署需优先控制长尾劣化风险，通过校准而非经验阈值选择压缩策略才能兼顾效率与可靠性。
