---
title: 'The Third Restructuring of Software Form: From the Three-Tier Architecture
  to Storage, Models, and Agents'
title_zh: 软件形态的第三次重构：从三层架构到存储-模型-Agent三元架构
authors:
- Wei Lin
- Tao Zhou
- Zhaofei Xie
- Changgui Hong
affiliations:
- Nanjing Liancheng Intelligent Technology Group
arxiv_id: '2608.20201'
url: https://arxiv.org/abs/2608.20201
pdf_url: https://arxiv.org/pdf/2608.20201
published: '2026-08-20'
collected: '2026-08-21'
category: Agent
direction: Agent原生软件架构范式演进与落地边界
tags:
- LLM
- Agent
- Software3.0
- LLM OS
- Database
- Architecture
one_liner: 提出Software 3.0范式下传统三层软件架构收敛为广义数据库、大模型、Agent三元结构的可验证框架与适用边界
practical_value: '- 电商/推荐系统可按「可表达性×重要性」拆分业务逻辑：非关键可表达规则（如推荐理由撰写、活动文案生成）交给LLM推理，强约束规则（如库存校验、权益发放规则）下沉为存储层约束，复杂核心逻辑（如排序召回内核）封装为Agent可调用的确定性工具，兼顾LLM灵活性与业务正确性

  - Agent化系统的正确性无需依赖LLM自身可靠性，可通过存储层的统一约束（事务、唯一性、前置校验规则）做最终兜底，如电商大促订单场景，存储层约束对LLM调度错误的拦截率可达100%，仅需毫秒级开销

  - 高并发低延迟的核心链路（如实时召回、交易扣费）暂不适合全Agent化，可采用「LLM离线生成代码+在线运行编译逻辑」的折中方案，平衡开发效率与性能要求'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM将自然语言转可执行行为的成本降至历史新低，传统三层软件架构（UI、业务逻辑、数据层）的存在前提被动摇。此前研究分别探索了LLM OS、Agent执行环、数据库与AI融合等方向，但缺乏对软件形态整体演进的统一框架及清晰适用边界，容易陷入“LLM万能”或“LLM无用”的极端认知。
### 方法关键点
- 提出收敛论断：满足适用条件的软件系统会从三层架构收敛为三元结构：广义数据库（所有持久化状态、约束、知识的统一抽象）、大模型（推理与生成核心）、Agent（连接前两者的计划-记忆-工具调用执行循环）
- 三层架构重构逻辑：UI层拆分为确定性状态投影层（如余额、合规提示）与模型生成装饰层（如布局、话术）；业务逻辑按「可表达性×临界性」拆分为三类：可表达非临界交LLM推理，临界可声明化下沉为存储约束，临界不可声明化保留为确定性工具
- 明确适用边界：仅当场景满足任务可表达可验证、状态外部化、工具边界完备、经济阈值四个条件时，三元架构成立，同时划定四类不适用场景：强确定性核心任务、高并发低延迟场景、强监管合规场景、结果不可验证场景
### 关键实验
- 模拟生产调度场景：上游规划器错误率达30%时，存储层约束可100%拦截非法请求，保证最终状态合法，单200次操作校验耗时仅1.1ms
- 真实LLM调度实验：Qwen-Plus直接生成排程的20次请求0%可行，存储层全部拦截；采用工具调用的10次请求100%返回正确结果
### 核心结论
正确性由存储层保障而非上游推理质量，LLM不需要绝对可靠，只要有合适的兜底机制就能落地到业务系统。
