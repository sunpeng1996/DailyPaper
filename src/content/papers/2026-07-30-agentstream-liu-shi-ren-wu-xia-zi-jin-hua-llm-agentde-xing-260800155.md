---
title: 'AgentStream: How Well Do Self-Evolving LLM Agents Perform Under Streaming
  Tasks?'
title_zh: AgentStream：流式任务下自进化LLM Agent的性能评估框架
authors:
- Dong Yan
- Jian Liang
- Dapeng Hu
- Ran He
- Nicholas Jing Yuan
- Qi Zhang
- Tieniu Tan
affiliations:
- 中国科学院大学
- Microsoft
- 中国科学院自动化研究所
- 南京大学
arxiv_id: '2608.00155'
url: https://arxiv.org/abs/2608.00155
pdf_url: https://arxiv.org/pdf/2608.00155
published: '2026-07-30'
collected: '2026-08-05'
category: Agent
direction: 自进化Agent · 流式任务评估
tags:
- LLM Agent
- Self-Evolution
- Streaming Task
- Evaluation Framework
- Test-time Learning
one_liner: 首个可配置流式任务评估框架，系统拆解自进化Agent性能的核心影响因素
practical_value: '- 场景-方法匹配：单域垂直Agent（如电商品类导购、专属客服）优先选上下文集成类自进化方法，收益最稳定；跨域多场景Agent（如全品类助手、通用服务）优先选检索式自进化方法，抗跨域干扰能力更强

  - 基座选型参考：自进化存在能力门槛，低能力基座叠加自进化会出现负收益；中等能力基座的自进化收益比强基座更高，投入产出比更优

  - 任务流调度优化：跨域任务流优先采用混排模式而非按领域顺序推送，整体效果稳定性提升，平均进化收益高20%以上

  - 方法选型：不要追求通用自进化方案，需针对所用基座单独测试最优方法，仅ReasoningBank类方法跨基座迁移性相对较好'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有自进化LLM Agent的评估均采用孤立单任务范式，无法反映真实部署中面临的跨域、流式、无明确任务边界的生产场景，自进化的真实收益、干扰因素均不明确，亟需贴近实际的评估体系。
### 方法关键点
- 提出AgentStream统一评估框架，支持可配置任务流与全类型自进化组件（上下文、记忆、技能、调度框架）的标准化评估
- 定义3类典型流式场景：Isolated（单域独立进化，无跨域经验迁移）、Sequential（按领域顺序处理，进化状态跨域传递）、Interleaved（全领域任务混排，共享进化状态）
- 覆盖5类主流自进化方法、3款前沿基座、6类覆盖工具调用、推理、交互等能力的Agent基准任务
### 关键结果
- 单域Isolated场景自进化正收益率75.7%，平均收益+1.37%，是风险最低的自进化场景
- 跨域场景中Interleaved比Sequential平均收益高20%，结果稳定性更强
- 自进化收益存在能力门槛：最弱基座GPT-5.4所有场景平均收益为负，中等基座Gemini 3.1 Pro平均收益+2.37%，反而高于更强的Claude Opus 4.7的+1.23%
- 上下文集成类方法在单域场景收益最高，检索式方法在跨域混排场景收益最高，不存在通用最优方法
### 核心结论
自进化Agent的收益不存在普适性方案，必须结合基座能力、任务流场景选择适配的自进化方法，不要在低能力基座上强行叠加自进化模块
