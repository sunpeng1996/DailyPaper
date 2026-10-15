---
title: 'AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety'
title_zh: AgentSafeEvo：面向LLM Agent安全的对抗协同进化框架
authors:
- Chenxu Wang
- Xiaoyu Wen
- Han Qi
- Ziyuan Zhou
- Cheng Jin
- Chaochao Lu
- Qiaosheng Zhang
affiliations:
- 上海人工智能实验室
- 复旦大学
- 上海交通大学
- 浙江大学
arxiv_id: '2610.19422'
url: https://arxiv.org/abs/2610.19422
pdf_url: https://arxiv.org/pdf/2610.19422
published: '2026-10-13'
collected: '2026-10-15'
category: Agent
direction: Agent安全 · 对抗协同进化
tags:
- LLM Agent
- Adversarial Training
- Co-Evolution
- Reinforcement Learning
- Safety Alignment
one_liner: 通过攻击者-防御者对抗协同进化RL框架，提升LLM Agent多轮工具交互场景的安全鲁棒性同时保留通用能力
practical_value: '- 电商/推荐类Agent做安全对齐时，可复用「安全+效用」双维度奖励设计，避免Agent为了合规过度拒绝合法用户请求，平衡安全性与业务体验

  - 多任务RL训练时可引入可学习性引导的任务加权机制，按单任务内reward方差分配训练权重，优先学习区分度高的任务，提升训练效率与效果

  - 业务Agent做红队攻防测试时，可参考论文覆盖的6大类13小类攻击场景（直接/间接prompt注入、工具描述注入等）构造测试用例，覆盖更多边界风险

  - 做Agent对抗训练时可采用GRPO做联合策略优化，同步迭代红队攻击生成与防御策略，避免静态攻击集导致的过拟合问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent安全对齐多聚焦语言层面风险，或仅针对固定任务的prompt注入攻击，未覆盖用户查询、工具描述、环境观测全链路攻击场景；静态对抗训练的攻击集固定，防御能力迭代时攻击能力无法同步进化，易出现过拟合，也无法暴露Agent在多轮工具交互中的隐性安全风险。

### 方法关键点
- 两阶段训练框架：第一阶段通过SFT初始化红队攻击者，生成覆盖6大类13小类攻击的对抗任务；第二阶段采用GRPO联合优化攻击者与防御者策略，攻击者生成对抗任务诱导防御者做出不安全行为，防御者学习在攻击下安全完成任务
- 双维度奖励设计：防御者奖励融合安全（是否出现不安全行为）与效用（是否完成合法任务要求），避免过度拒绝；攻击者奖励为同任务下防御者平均奖励的负值，形成零和博弈
- 可学习性引导的任务加权：按单任务内防御者reward的标准差分配权重，方差越大的任务权重越高，优先给区分度高的任务分配训练资源，协调攻击生成与防御学习节奏

### 关键结果
在Agent-SafetyBench、AgentHarm等4个安全基准上，对比静态对抗训练基线，攻击成功率（ASR）在Agent-SafetyBench上从31.01%降至17.84%，AgentHarm的harm score从30.00降至6.53；同时通用能力不降反升，ALFWorld准确率从30.89%升至43.72%，ToolHop准确率从39.43%升至48.04%，基础函数调用能力基本无损失。

**最值得记住的一句话**：对抗协同进化不仅能提升LLM Agent的安全鲁棒性，进化过程中生成的高难度任务还能为Agent的通用工具使用、规划能力提供有效训练信号。
