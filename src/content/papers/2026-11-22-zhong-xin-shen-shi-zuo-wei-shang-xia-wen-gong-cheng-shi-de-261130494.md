---
title: Revisiting LLMs as Context Engineers
title_zh: 重新审视作为上下文工程师的大语言模型
authors:
- Junrui Zhang
- Zeyu Xu
- Runchuan Zhu
- Jie Peng
- Long Zhang
- Zixin Ding
- Jiaxin Lin
- Kai Wang
- Jianmin Ji
- Junyuan Hong
affiliations:
- National University of Singapore
- University of Science and Technology of China
- University of Chicago
- Independent Researcher
arxiv_id: '2611.30494'
url: https://arxiv.org/abs/2611.30494
pdf_url: https://arxiv.org/pdf/2611.30494
published: '2026-11-22'
collected: '2026-11-27'
category: LLM
direction: LLM 上下文工程能力评估
tags:
- Context Engineering
- LLM Benchmark
- Prompt Optimization
- Reasoning
- Instruction Adherence
one_liner: 构建多推理模式基准，揭示LLM自动上下文工程的适用边界与核心瓶颈
practical_value: '- 业务中使用LLM自动优化prompt前，先评估当前任务推理失败模式的多样性，多样性越高（如多轮用户query理解、非标商品推荐），LCE方法增益越低，优先用人工精调prompt

  - 可复用结论：LCE的核心增益来自提升LLM指令遵循度，若当前业务LLM已经符合指令要求，无需额外引入LCE流程增加算力开销

  - 做Agent的自动prompt迭代时，不要盲目堆模型参数或迭代次数，优先收敛失败模式的类型，再用LCE方法抽取优化经验，提升迭代效率'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
LLM自动上下文工程（LCE）通过让LLM从离线试错中抽取通用经验优化上下文，无需大量训练即可适配下游任务，但生效条件、能力边界尚未明确，缺乏系统性评估。
### 方法关键点
搭建覆盖不同推理模式的LCE专属基准，对比多种LCE方法在不同系列8B参数LLM上的表现，验证参数规模、生成迭代次数对效果的影响，分析性能与推理失败模式多样性的相关性。
### 关键结果
- 无跨任务通用最优LCE方法，部分场景效果甚至不及Chain-of-Thought等简单baseline，扩参数、增迭代次数也无法稳定提升LCE效果
- LCE性能增益与推理轨迹失败模式多样性显著负相关（r=-0.5，p≤0.05）
- LCE增益部分来自指令遵循度提升，核心瓶颈是LLM无法从高度多样化的失败中抽取有效通用经验
