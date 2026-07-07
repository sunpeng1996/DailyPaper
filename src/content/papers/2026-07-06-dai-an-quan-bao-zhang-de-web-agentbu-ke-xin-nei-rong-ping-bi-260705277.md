---
title: Untrusted Content Masking for Web Agents with Security Guarantees
title_zh: 带安全保障的Web Agent不可信内容屏蔽方案
authors:
- Kristina Nikolić
- Egor Zverev
- Javier Rando
- Matthew Jagielski
- Edoardo Debenedetti
- Florian Tramèr
affiliations:
- ETH Zurich
- ISTA
- Anthropic
arxiv_id: '2607.05277'
url: https://arxiv.org/abs/2607.05277
pdf_url: https://arxiv.org/pdf/2607.05277
published: '2026-07-06'
collected: '2026-07-07'
category: Agent
direction: Web Agent安全 · 提示注入防御
tags:
- Web Agent
- Prompt Injection
- DOM
- Privilege Separation
- Security Defense
one_liner: 基于DOM信任边界划分的不可信内容屏蔽+隔离结构化查询方案，实现Web Agent提示注入零攻破同时保留任务效用
practical_value: '- 电商导购Web Agent可直接复用UCM架构：先基于DOM标记用户评论/UGC/第三方广告等不可信区域做掩码，避免恶意注入内容篡改导购逻辑（如诱导跳转竞品、下单非目标商品）

  - 涉及UGC内容的Agent任务可部署双模型隔离架构：主Agent仅处理可信站点内容，需读取UGC时调用仅返回结构化类型（bool/int/enum等）的隔离Q模型，完全阻断自由文本注入风险

  - 无站点手动标注的场景可复用自动化边界推理方案：先对DOM做内容脱敏（仅保留结构、标签、类名）后调用LLM生成不可信区域的CSS选择器，Reddit场景下F1可达0.997，部署成本极低

  - 高敏感Agent任务可叠加二次校验：对于Q模型返回的聚合类结果（如商品好评率、评分均值）可并行查询多个元素，出现异常匹配时触发用户确认，规避数据流篡改风险'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有Web Agent防御prompt注入的方案要么是启发式检测无 formal 安全保障，易被自适应攻击绕过；要么完全隔离不可信内容导致任务效用严重下降，无法适配电商导购、行程预订等同时需要处理可信站点结构与不可信UGC/第三方内容的场景。

### 方法关键点
- 利用DOM结构天然的信任边界信息，在页面渲染给主Agent前将不可信区域替换为带唯一ID的占位符，从架构上消除主Agent接触注入内容的攻击面
- 设计隔离的Quarantined Model（Q模型）：主Agent需读取不可信内容时，仅传递元素ID、查询问题、预设返回类型（bool/int/float/enum/date），Q模型仅返回符合类型约束的结构化结果，完全阻断注入指令回传主Agent的路径
- 针对无手动标注的站点，先对DOM做内容脱敏（移除所有文本、匿名化属性值），调用LLM识别不可信区域的CSS选择器，自动生成信任边界

### 关键实验结果
在10个自定义站点（含电商、银行、论坛等）和WebArena GitLab套件上评测，对比无防御基线：所有增强WASP prompt注入攻击全部被阻断，攻击成功率0%；无需访问不可信内容的任务效用完全保留，成本开销最低1.05x；需要访问不可信内容的任务效用无明显下降，成本开销最高1.84x；自动化边界推理在Reddit站点F1达0.997，Booking、GitLab也分别达到0.879、0.840。

> 最值得记住的一句话：从架构上隔离可信指令与不可信数据，是比启发式检测更可靠的LLM Agent安全防御路径。
