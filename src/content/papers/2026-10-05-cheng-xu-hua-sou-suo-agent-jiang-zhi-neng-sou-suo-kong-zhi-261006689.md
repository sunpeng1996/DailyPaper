---
title: 'Programmatic Search Agents: Extending Agentic Search Beyond Query Reformulation'
title_zh: 程序化搜索Agent：将智能搜索控制范围拓展到查询改写之外
authors:
- Jiaming Qian
- Huiyan Yang
- Mandi Liu
- Jie Liu
- Wenkai Shen
- Pengyang Zhou
- Jing Jin
- Jin Ma
- Dezhi Ye
- Chaochao Chen
affiliations:
- Zhejiang University
- Tencent Yuanbao Team
- Peking University
arxiv_id: '2610.06689'
url: https://arxiv.org/abs/2610.06689
pdf_url: https://arxiv.org/pdf/2610.06689
published: '2026-10-05'
collected: '2026-10-06'
category: Agent
direction: 搜索Agent · 可编程检索流程控制
tags:
- Search Agent
- Programmatic Search
- Retrieval Pipeline
- Evidence Management
- LLM Agent
one_liner: 提出以候选集可执行计算为搜索动作单元的PSA框架，提升搜索Agent成功率并降低token消耗
practical_value: '- 搜索/推荐场景的Agent可复用PSA的持久化候选工作空间设计，全局存储召回的商品/内容候选，避免重复召回浪费算力，同时支持跨轮次的过滤、重排、信息抽取操作

  - 电商导购/客服Agent的检索流程可借鉴可编程单元设计，将查询改写、召回、过滤、重排、片段提取封装为可组合原子操作，根据用户意图动态编排执行流，无需每一步都调用LLM决策，降低交互延迟和token消耗

  - 长会话推荐/搜索场景可参考选择性证据返回机制，仅将当前决策需要的信息返回给LLM上下文，候选全集保留在外部工作空间，既降低上下文窗口占用，又不会丢失潜在有用候选'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有搜索Agent仅能控制查询改写，召回、重排、证据返回全由固定搜索流水线决定，轨迹分析显示42.7%已进入抽取阶段的支撑证据从未被返回给Agent，同页Oracle实验显示修复完全缺失的证据可提升任务成功率16.7个百分点、减少后续搜索决策64%，瓶颈已从证据检索转向已召回证据的处理与呈现。

### 方法关键点
- 持久化候选工作空间：召回的候选对象全局存储，仅暴露变量名、类型、大小等元信息给LLM，无需全量进入上下文，支持跨轮次复用
- 灵活原语组合：封装retrieve、filter、rerank、extract、dedupe 5个原子操作，LLM生成包含条件、循环的可执行Python代码单元，运行时自动解析单元内的数据依赖，无需每步操作都触发LLM决策
- 选择性证据呈现：每个代码单元可自定义返回给LLM的观察结果，无需全量返回处理后的所有候选，大幅降低上下文token占用

### 关键实验
在InfoSeek-Eval、BrowseComp-Plus两个搜索基准上，与基于固定查询的Agent、基于工具调用的Agent对比，覆盖5个主流LLM backbone，无任务特定训练：相对基于查询的Agent，PSA在两个基准上任务成功率分别提升4.00、7.56个百分点，最终步骤token平均降低28.3%、33.9%；相对同样支持原语和持久化空间的工具调用Agent，PSA成功率仍有提升，token平均降低46.3%、54.5%。

最值得记住的一句话：搜索Agent的优化不能仅局限于查询改写能力，将检索流水线的控制权下放给Agent、让其按需编排候选处理逻辑，可在不增加底层检索算力的前提下实现效果与效率的双重提升。
