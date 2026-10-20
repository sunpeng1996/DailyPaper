---
title: 'ASTOR: Benchmarking and Improving Autoformulation for Soft-Constraint Optimization
  with a Formal Grammar'
title_zh: ASTOR：基于形式语法的软约束优化自动建模框架与基准
authors:
- Amer Goel
- Yeganeh Alimohammadi
- Andrew Daw
arxiv_id: '2610.26819'
url: https://arxiv.org/abs/2610.26819
pdf_url: https://arxiv.org/pdf/2610.26819
published: '2026-10-19'
collected: '2026-10-20'
category: Agent
direction: Agent 决策约束自动建模优化
tags:
- AST
- Formal Grammar
- Soft Constraint Optimization
- Benchmark
- LLM Agent
one_liner: 提出支持软硬约束优化的ASTOR推理框架与软约束建模基准SoftOR，精度超过现有单请求及多智能体方法
practical_value: '- 开发电商购物Agent、行程规划Agent时，可引入本文的软硬约束区分逻辑，将用户的「必须」类硬约束、「最好」类软约束拆分为不同优先级的优化目标，既不妥协核心需求，也能最大化满足用户偏好，提升推荐/决策满意度

  - LLM生成可执行代码、结构化查询等输出时，可复用「形式语法约束+AST中间表示+确定性编译」的 pipeline，降低生成语法错误、逻辑错误的概率，减少后续调试成本

  - 评估Agent决策合理性时，可借鉴SoftOR的评估思路，基于自然语言中的模态词区分约束优先级，用决策的目标值匹配度替代主观人工评估，提升评估的客观性和自动化程度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM自动优化建模方法与基准多聚焦必须满足的硬约束，忽略电商购物、行程规划、排班等实际场景中大量存在的用户偏好类软约束，无法区分刚性要求与可妥协的偏好，也无法对优先级不同的偏好排序，导致Agent决策经常不符合用户预期。
### 方法关键点
- 提出ASTOR推理框架：仅需单次LLM调用，引导LLM输出符合自定义形式语法的抽象语法树（AST），再通过确定性流程验证AST合法性、编译为Gurobi可执行的优化代码，无需额外微调或多轮交互
- 发布SoftOR基准：覆盖护士排班、COMPASS、TravelPlanner、LexiBench共355个软约束优化实例，支持加权惩罚、字典序两种主流软约束建模方式，基于模态词（必须/强烈偏好/偏好）标注约束优先级，提供求解器验证的金标准最优值
### 关键结果
- 在SoftOR基准上，ASTOR的解准确率达88.5%，比最强基线多智能体方法CoE高3.7个百分点，调用成本比CoE低10.3%；在435个传统硬约束基准上准确率达81.8%，与最优基线性能差小于0.5个百分点，无明显性能损失
- ASTOR的总错误率为所有对比方法最低，在模态词隐式标注优先级的场景下优势尤为突出
### 核心结论
用形式化中间表示约束LLM输出结构，是提升决策类Agent建模准确率、降低生成错误的高性价比方案
