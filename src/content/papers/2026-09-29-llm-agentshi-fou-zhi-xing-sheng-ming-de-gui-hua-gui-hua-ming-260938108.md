---
title: Do LLM Agents Execute the Plans They Declare? From Planning-Mode Declaration
  to Pattern-Specific Execution
title_zh: LLM Agent是否执行声明的规划？规划声明到模式专属执行研究
authors:
- Subba Reddy Oota
- Francisco Herrera
- Jordi Cabot Sagrera
- Marcos López de Prado
- Shadab Khan
affiliations:
- ADIA Lab
- University of Granada
- Luxembourg Institute of Science and Technology
- Cornell University
- Lawrence Berkeley National Laboratory
arxiv_id: '2609.38108'
url: https://arxiv.org/abs/2609.38108
pdf_url: https://arxiv.org/pdf/2609.38108
published: '2026-09-29'
collected: '2026-09-30'
category: Agent
direction: Agent 规划执行一致性优化
tags:
- LLM Agent
- Planning
- ReAct
- Task Routing
- Execution Fidelity
one_liner: 提出规划即路由框架，将LLM声明的规划模式路由至匹配的专属执行器，缩小规划声明执行gap
practical_value: '- 搭建电商/推荐场景Agent（如全链路导购、多条件商品筛选、售后处理Agent）时，不要仅依赖纯ReAct架构：短平快查询类任务用Predefined模式，长链路复杂任务（如跨店凑单、多维度比价）用Hierarchical或Search模式，相比Plan+ReAct最高可提升91.7%的任务成功率

  - 可直接复用「规划即路由」架构：先让LLM输出任务对应的规划模式，通过硬规则路由到对应模式的专属执行器，强制执行流程匹配规划结构，彻底避免纯prompt引导的规划执行偏离问题，长任务下效果提升尤为明显

  - 规划模式选择无需追求per-task动态选型，可先做场景级的固定模式匹配：比如搜索Query意图理解用Sequential模式，复杂用户问题解答用Hierarchical模式，性能接近最佳固定模式，实现成本远低于动态路由

  - 不要迷信LLM生成的规划文本质量评分，实测评分与最终任务成功率的相关性低于0.18，优先选择和场景匹配的规划模式，而非只看规划文本的合理性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM Agent的规划-执行架构存在两类核心痛点：一是即使将规划写入prompt传入ReAct执行器，也无法保证执行过程不偏离声明的规划结构，二是仅用最终任务成功率无法区分失败源于规划模式选择错误还是执行跑偏，同时业界缺乏针对不同任务匹配最优规划模式的通用落地方案。

### 方法关键点
- 定义4类通用规划模式：Predefined（生成固定全量计划、执行中不重规划）、Sequential（按步执行+根据中间反馈动态重规划）、Hierarchical（目标分解为子任务，采用编排器+worker架构执行）、Search（生成多份候选计划，分别执行后通过打分选择最优轨迹）
- 提出Planning-as-Routing框架：LLM先声明当前任务适配的规划模式，通过确定性硬路由直接分发到对应模式的专属执行器，执行流程强制匹配规划结构，从根源避免执行偏离
- 配套规划执行验证框架，可精准区分「规划模式选择失败」和「执行偏离失败」两类错误，方便问题定位

### 关键结果
- 实验覆盖4个主流Agent基准（ALFWorld、Mind2Web、SWE-bench、WebArena）、3款开源LLM（Qwen3.6、DeepSeek-V4、Gemma-4），对比Flat ReAct、Plan+ReAct两类基线
- 通用Plan+ReAct仅22%~45%的轨迹能保持声明的规划结构，长规划（>6步）场景下结构保持率低于10%
- 模式专属执行器相比Plan+ReAct，ALFWorld任务成功率从0.48提升至0.92，SWE-bench Verified任务成功率从0.36提升至0.44；few-shot示例可提升规划模式选择准确率，增益最高达+0.16

### 核心结论
让LLM做规划选型、用硬规则绑定对应执行器的架构，远好于把规划塞到prompt里让ReAct自由执行的方案，长任务下优势尤其明显
