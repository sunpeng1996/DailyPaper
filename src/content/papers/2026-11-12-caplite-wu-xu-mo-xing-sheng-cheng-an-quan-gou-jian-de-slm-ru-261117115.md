---
title: 'CapLite: Prompt-Injection Defense for Small Language Model Agents without
  Model-Written Security Artifacts'
title_zh: CapLite：无需模型生成安全构件的SLM Agent Prompt注入防御框架
authors:
- Zimo Xu
- Wenzhuo Liu
- Hideki Nakayama
affiliations:
- The University of Tokyo
- Institute of Automation, CAS
arxiv_id: '2611.17115'
url: https://arxiv.org/abs/2611.17115
pdf_url: https://arxiv.org/pdf/2611.17115
published: '2026-11-12'
collected: '2026-11-13'
category: Agent
direction: Agent 轻量Prompt注入防御方案
tags:
- Prompt Injection Defense
- SLM Agent
- Tool Calling
- Security Policy
- Authorization
one_liner: 基于工具Schema和用户请求做确定性授权，实现15款SLM Agent 0 Prompt注入攻击成功率
practical_value: '- 电商/广告场景中涉及写操作的Agent（发券、改用户标签、下单等），无需让SLM生成权限策略，直接从工具Schema按固定规则提取读写分类、敏感参数字段，可大幅降低注入风险

  - 计划阶段提前锁死所有写操作，读阶段不允许新增/修改写操作，敏感参数（收券人ID、优惠金额、商品ID）严格匹配用户原始请求的精确值，无需额外模型开销即可防注入

  - 1.7B-35B区间SLM生成的安全构件（策略、执行图）错误率、被攻击成功率随模型尺寸上升反而升高，确定性代码校验比模型生成策略可靠得多'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Prompt注入防御大多依赖Agent自身模型生成安全构件（权限策略、执行依赖图、运行代码等），但1.7B~35B参数的SLM生成的这类构件错误率极高：Progent的生成策略在14/15款测试模型上可被攻破，CaMeL生成的代码最高68%无法运行，且模型越大被注入成功率越高，亟需不依赖模型生成安全构件的低开销防御方案。

### 方法关键点
- 自动从工具Schema生成安全策略：按动词自动分类读写工具，识别出敏感权限字段（收方ID、金额、对象ID、URL等）、非敏感字段（文本内容、时间、枚举值），未分类工具直接拦截
- 读写分离+写操作预提交：仅可见用户请求的Planner提前生成所有写操作并锁死，读阶段仅允许执行只读工具，不允许新增/修改写操作
- 确定性参数校验：写操作执行前所有敏感权限字段必须和用户原始请求的精确值完全匹配，不匹配则拦截或请求用户确认

### 关键实验
基于AgentDojo基准测试，覆盖15款1.7B~35B开源模型，对比CaMeL、Progent等SOTA防御：
- CapLite在13935个攻击样本上攻击成功率（ASR）为0，是唯一全量测试模型无攻破的方案
- 受攻击下效用（UA）29.0%与CaMeL的27.2%相当，单episode token消耗仅17.1k，为CaMeL的18%，效用token比1.69为所有防御方案最高

> 最值得记住的一句话：1.7B~35B区间的SLM无法可靠生成自身的安全防御构件，确定性代码层面的读写隔离+参数校验，比依赖模型生成的安全策略更可靠、成本更低
