---
title: 'PHRBench: A Behavioral Evaluation of Post-Hallucination Reasoning in LLMs'
title_zh: PHRBench：大语言模型幻觉后推理的行为评估基准
authors:
- Linghao Meng
- Feng He
- Xuan Yang
- Junyuan Mao
- Pinze Ren
- Deqing Mu
- Hesen Yang
- Qiankun Li
affiliations:
- National University of Singapore
- Independent Researcher
- Tsinghua University
- Johns Hopkins University
- Nanyang Technological University
arxiv_id: '2610.10455'
url: https://arxiv.org/abs/2610.10455
pdf_url: https://arxiv.org/pdf/2610.10455
published: '2026-10-07'
collected: '2026-10-08'
category: Eval
direction: 大模型幻觉评估 · 推理行为量化
tags:
- Hallucination
- LLM Evaluation
- Post-Hallucination Reasoning
- Benchmark
- Reasoning Dynamics
one_liner: 提出幻觉后推理行为化基准PHRBench，覆盖4域18模型可提前预测幻觉修正成功率
practical_value: '- Agent多阶段链路中可复用论文的幻觉修正预测能力，上游漏检幻觉时提前判断下游能否自行修正，减少不必要的召回/重跑操作，降低链路耗时

  - 可引入Belief Update Frequency (BUF)指标优化CoT推理的幻觉校验逻辑，BUF高于阈值时说明模型正在主动修正冲突，可跳过冗余的外部事实校验步骤

  - 构建业务场景大模型评估集时，可复用3类幻觉注入范式（规则冲突、状态扭曲、伪科学纠缠），更全面测试模型对错误上下文的鲁棒性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前大模型幻觉无法100%被上游检测拦截，会流入多阶段LLM系统、Agent工作流作为后续推理的上下文，现有幻觉后推理（PHR）研究仅关注最终结果变化，无法区分模型对幻觉前提的不同处理行为，易将偶然答对误判为成功修正幻觉，缺乏结构化的行为级评估框架。
### 方法关键点
- 构建PHRBench基准，覆盖化学、生物医学、物理、代码生成4个领域，共4820个控制实例，每个问题搭配1个真实上下文和3类幻觉上下文（规则冲突、状态扭曲、伪科学纠缠）
- 提出行为级评估框架，独立于最终答案正确性，将推理轨迹分为幻觉依从、幻觉规避、启发式修正3类，额外定义成功修正并答对的为「洞察轨迹」
- 设计输出长度、不确定指数、信念更新频率（BUF）、分支复杂度4项指标，量化推理过程动态
- 基于prompt结构+语义特征训练轻量XGBoost预测器，提前预判洞察轨迹出现概率
### 关键结果
- 测试18款开源/闭源LLM，幻觉上下文平均使准确率下降7.7pct，模型越大准确率下降越显著（GPT-5.2降幅达16.9pct），但大模型启发式修正行为占比更高，存在鲁棒性与修正能力的权衡
- 成功修正的洞察轨迹占比极低，11/18模型占比低于10%，最高的Qwen3-235B也仅24.91%；洞察轨迹的BUF比非洞察轨迹高2.5倍，是核心区分特征
- 轻量预测器预测洞察轨迹的AUROC达0.847，prompt总长度、领域规则冲突、错误局部性是TOP3特征

最值得记住的结论：大模型越强越容易被错误上下文误导，仅识别幻觉不足以解决问题，只有触发有效的信念更新调整后续推理才能真正修正幻觉。
