---
title: 'RecoGEM: A Serving System for Production-Scale Generative Recommendation'
title_zh: RecoGEM：面向生产级规模的生成式推荐服务系统
authors:
- Xiangrui Yang
- Yunfeng Zhao
- Jiawei Yang
- Fangyu Zhang
- Enrui Zhao
- Liang Zeng
- Cheng Peng
- Minhui Xie
- Jiaqiang Liu
- Xiao Liang
affiliations:
- The University of Hong Kong
- Kuaishou Technology
- Peking University
- Renmin University of China
arxiv_id: '2611.12296'
url: https://arxiv.org/abs/2611.12296
pdf_url: https://arxiv.org/pdf/2611.12296
published: '2026-11-09'
collected: '2026-11-10'
category: GenRec
direction: 生成式推荐 · 工业级服务系统
tags:
- Generative Recommendation
- Serving System
- Semantic ID
- Beam Search
- KV Cache
one_liner: 提出runtime与引擎解耦的生成式推荐专属服务系统，性能较基准提升2.88倍，支撑亿级用户生产落地
practical_value: '- 架构设计可复用runtime-引擎解耦思路：将GR专属的步骤跳转、候选状态管理、在线更新逻辑剥离到独立runtime，引擎仅负责张量计算，同时兼顾与现有传统推荐栈的兼容性

  - 算子优化层面，针对生成式推荐短KV前缀、大量独立候选的特征，可替换通用SDPA为Row-Tiled Self-Attention，短序列场景下性能最高提升154倍

  - 候选选择阶段采用「beam行局部TopK预剪+全局TopK」的两阶段radix选路，比通用TopK性能提升1.4~2.24倍，大幅降低beam search临界路径延迟

  - 工程实现可复用预编译step粒度执行计划+版本校验无感知切流方案，支持模型权重、SID词表、选数策略的高频在线更新，避免更新引发的延迟尖刺'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式推荐（GR）通过自回归生成Semantic ID直接输出推荐结果，绕过传统推荐召回排序的候选池限制，效果更优，但与现有服务栈存在多重适配矛盾：GR解码步骤异构（每步词表、张量形状均不同）、需高频更新模型/词表/选数策略，且短序列、大候选集的特征与LLM长序列优化方向相悖，直接复用LLM服务框架或传统推荐栈性能不达标，无法满足工业级时延吞吐要求。

### 方法关键点
- 采用runtime与引擎解耦架构：runtime负责解码步骤调度、候选状态管理、在线artifact更新，引擎专注张量计算，通过自动生成的部署契约规范二者交互
- 行分块自注意力优化：将多个短注意力行打包为一个执行块，分摊kernel启动开销，融合计算逻辑减少访存
- 步骤粒度执行规划：提前探测每个解码步骤的张量形状，编译生成适配每步特征的专属执行计划，避免通用动态形状的性能损耗
- 两阶段快速候选选择：先按beam行做局部TopK预剪，再做全局TopK，适配GR大候选集beam search场景

### 关键结果
在快手生产环境部署9个月以上，覆盖4亿日活用户的搜索、广告、推荐场景，支持10+GR模型族；单实例0.2B参OneModel workload下QPS超1000，P99时延低于35ms，吞吐较通用生成服务基准提升2.88倍；集群峰值QPS达6万，MFU达55.3%，高频在线更新无明显时延尖刺。

**最值得记住的一句话**：生成式推荐服务不能直接复用LLM服务栈，针对GR短序列、大候选、步骤异构、更新频繁的特征做专属优化，可获得数倍的性能提升。
