---
title: 'Macaron-V1: Towards Open Continual Learning with Self-Improvement and Mixture-of-LoRA'
title_zh: Macaron-V1：基于Mixture-of-LoRA与自提升的开放持续学习Agent框架
authors:
- Mind Lab
- Vin Bo
- Asher Cai
- Jingwei Cao
- Song Cao
- Vic Cao
- Amelia Chen
- Andrew Chen
- Kaijie Chen
- Cleon Cheng
affiliations:
- Mind Lab
arxiv_id: '2608.09819'
url: https://arxiv.org/abs/2608.09819
pdf_url: https://arxiv.org/pdf/2608.09819
published: '2026-08-09'
collected: '2026-08-11'
category: Agent
direction: Agent持续学习 · Mixture-of-LoRA
tags:
- LoRA
- Mixture-of-LoRA
- Continual Learning
- Agent
- Self-Improvement
one_liner: 提出冻结基座的Mixture-of-LoRA架构与递归自提升循环，实现部署后可迭代的开放持续学习Agent
practical_value: '- 多场景业务Agent可直接复用MoL架构：冻结通用基座，分别训练导购、客服、售后、内容生成等专属LoRA，路由按query自动切换，相比部署4个独立模型降低74%存储开销

  - 迭代流程可参考模型-Harness协同设计：将业务Agent的工具集、prompt、上下文规则做成版本化可迭代对象，先通过配置优化解决80% bad case，再用优质轨迹训练LoRA，大幅降低迭代成本

  - 工程实现可直接复用路由+KV缓存trick：用主LoRA加约束解码做路由，无需单独训练路由模型，准确率可达99%以上；每个LoRA维护专属对话视图，同场景重入时直接复用KV缓存，降低延迟'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前大模型后训练常绑定固定任务与环境，部署后无法基于真实交互持续迭代，多任务联合训练还会出现参数冲突，无法满足Agent在真实场景下长期服务用户、动态适配新需求的体验型智能要求。

### 方法关键点
- 架构采用Mixture-of-LoRA（MoL）：冻结大模型基座，训练多个垂直场景专属LoRA适配器，由Chat场景的L0 LoRA通过约束解码实现每轮请求的路由选择，无需单独训练路由模型；每个LoRA维护专属对话视图，仅保留其他LoRA的交互摘要，实现跨适配器上下文连续的同时支持KV缓存复用。
- 算法采用模型-Harness协同设计与递归自提升循环：将工具集、GenUI框架、上下文协议等运行时环境作为一等优化对象，通过Harness Context Protocol实现配置版本化，先做配置搜索解决bad case，再基于优质交互轨迹更新LoRA参数，实现部署后持续迭代。
- 旗舰版Macaron-V1-Venti基于744B GLM-5.2基座，搭载聊天、Agent、代码、GenUI四个1B参数LoRA；轻量化版基于50B Qwen3.6基座，适配本地部署。

### 关键结果
路由准确率达99.12%，路由+摘要额外开销仅占总延迟的32%；相比部署4个独立合并模型，MoL架构存储开销降低74%；配置搜索阶段对122个基座失败任务的覆盖率从9%提升至100%；GenUI场景下相比原生HTML生成输出token减少45%，首渲速度最高提升6倍。

最值得记住的一句话：Agent的迭代优化要走「orchestration over merging」的路线，通过路由编排实现能力组合，远比合并多任务参数的泛化性和迭代效率更高。
