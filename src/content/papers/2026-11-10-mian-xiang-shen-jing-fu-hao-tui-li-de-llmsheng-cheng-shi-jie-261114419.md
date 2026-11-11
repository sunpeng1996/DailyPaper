---
title: Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning
title_zh: 面向神经符号推理的LLM生成世界模型评估方法
authors:
- Souhaila Djaffal
- Amna Jamal
- Gagana Madhugiri Devaraja
- Anidipta Pal
- Jobst Heitzig
affiliations:
- PRISM AI Safety Research
- Potsdam Institute for Climate Impact Research
arxiv_id: '2611.14419'
url: https://arxiv.org/abs/2611.14419
pdf_url: https://arxiv.org/pdf/2611.14419
published: '2026-11-10'
collected: '2026-11-11'
category: Eval
direction: 神经符号推理 · LLM世界模型评估
tags:
- World Model
- Neuro-Symbolic Reasoning
- LLM Evaluation
- POSG
- Multi-agent
one_liner: 提出三维度评估框架与44场景基准，证明机械有效不代表世界模型忠实
practical_value: '- 业务中落地Agent规划用的世界模型生成流程时，不能仅做语法/可执行性校验，必须补充结构对齐校验+语义合规校验三层逻辑，避免生成的可运行模型和实际业务场景（比如电商导购、广告投放规则）出现核心偏差

  - 做跨地域/文化的电商推荐、跨境服务Agent时，显式的国家/地域标签会显著改变LLM生成的世界模型结构，即使语义检查通过，也可能隐含不符合本地规则的假设，必须单独做本地化规则校验

  - LLM生成结构化业务产物（比如规则JSON、流程模型、世界模型）时，即使temperature设为0，多次生成结果仍可能存在显著结构差异，业务落地时需要增加多轮一致性校验，不要依赖单次生成结果'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
神经符号系统依赖形式化世界模型支撑规划、安全校验等能力，但人工为每个场景构建世界模型效率极低，LLM自动生成是可行落地路径。现有评估仅校验机械可执行性，无法保证生成模型忠实反映真实场景，尤其多Agent、开放场景下偏差会直接导致下游推理完全偏离实际需求。
### 方法关键点
- 定义**POSG（部分可观测随机博弈）**作为世界模型统一输出格式，支持JSON结构化输出、Python可执行类两种实现形式
- 设计三层递进评估框架：机械有效性校验可执行性、状态/动作合法性、转移概率归一化、死态率等指标；结构保真度在有参考时计算排列不变的结构F1，无参考时做拓扑特征诊断；语义充分性基于预设必选/禁止特征做合规校验
- 构建44场景基准数据集，覆盖玩具环境、已知规则游戏、开放情境、文化相关场景四大类
### 关键结果
测试5款主流LLM（GPT-5.6 Sol、Claude Opus 5、Llama 3.3 70B、Qwen 3.8 27B、DeepSeek V4 Flash）的410次首次生成结果：
1. 游戏赛道135次生成中134个通过机械校验，但平均排列不变结构F1仅0.366，仅28个与参考完全匹配
2. 文化赛道中显式标注国家会使4款LLM的结构F1最高下降0.144，但语义评分变化仅±0.02，语义检查完全无法发现结构偏差
3. 相同prompt设temperature=0时，同LLM同场景多次生成的结构F1标准差最高达0.786，存在显著波动
### 核心结论
可执行性是LLM生成世界模型的必要不充分条件，仅通过机械校验的模型仍可能和真实场景存在本质结构偏差，直接用于下游推理会带来不可控风险
