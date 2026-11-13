---
title: Goal Encoding in LLMs
title_zh: 大语言模型内部目标编码的定位与实现机制研究
authors:
- Arnab Sen Sharma
- Eric Todd
- Sheridan Feucht
- Andy Arditi
- Rohit Gandikota
- Natalie Shapira
- Gabriele Sarti
- Constanza Fierro
- Lisa Schut
- David Bau
affiliations:
- Northeastern University
- Parallax
- University of Copenhagen
- University of Oxford
arxiv_id: '2611.17297'
url: https://arxiv.org/abs/2611.17297
pdf_url: https://arxiv.org/pdf/2611.17297
published: '2026-11-12'
collected: '2026-11-13'
category: LLM
direction: LLM 可解释性 · 目标编码
tags:
- LLM Interpretability
- Attention Head
- Goal Encoding
- Non-Recurrent Goal Seeking
- Causal Intervention
one_liner: 定位到LLM中编码目标的稀疏注意力头，揭示Transformer非递归目标追寻的实现机制
practical_value: '- 做Agent多步任务规划时可复用NRGS机制，无需硬维护长序列状态，每步从任务prompt和已执行上下文重新推导当前子目标，大幅降低状态传递复杂度

  - 生成式推荐/广告文案可控性优化场景，可定位对应任务的目标头，通过干预目标头的KV读取定向 steer 生成方向，成本远低于全模型微调

  - 电商/广告Agent的风险防控场景，可借鉴GOALSCOPE探针思路，提前读取模型隐式生成意图，在风险内容生成前完成拦截'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
业界长期争论LLM的目标导向行为是否对应显式内部目标表征，且Transformer无循环结构无法长期传递状态的特性，也与观测到的LLM多步长任务中目标持续的现象存在矛盾，厘清目标编码机制对LLM可控性优化、Agent规划迭代、生成内容风险防控都有核心价值。

### 方法关键点
- 基于Bratman规划理论定义目标三属性：预承诺、可塑性、持久性，选取多步代码生成场景作为可控测试环境
- 通过跨语言移植实验定位到稀疏的「目标头」注意力集合，基于Patchscope构建GOALSCOPE探针，可读取目标的自然语言描述
- 提出非递归目标追寻（NRGS）假说：LLM不会携带目标状态向前传播，而是每步重新读取任务prompt、比对已执行进度推导当前子目标
- 通过激活补丁、KV移植、query移植三类因果干预验证机制有效性

### 关键结果
基于Qwen-2.5-Coder-32B-Instruct测试：
- 目标头可在子目标执行前3个token以90%+准确率读取出即将执行的子目标，跨语言移植触发相同操作的平均成功率达87%
- 仅保留122个目标头对任务描述的访问权限时，模型子目标实现成功率接近基线的0.92；干预目标头读取的任务KV可实现94%的跨语言目标转向
- 非代码场景下，GOALSCOPE对few-shot ICL隐式规则的读取准确率最高达80%+，平均36.2%

最值得记住的结论：Transformer不需要循环结构即可实现长序列目标持续，靠每步重读任务+比对进度的非递归机制就能实现功能等价的目标追寻
