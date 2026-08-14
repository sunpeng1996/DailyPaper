---
title: 'LLMRouter: Unified Infrastructure for Developing, Evaluating, and Deploying
  LLM Routers'
title_zh: LLMRouter：LLM路由器开发、评估与部署的统一基础设施
authors:
- Tao Feng
- Fangxu Yu
- Haozhen Zhang
- Zhongjie Dai
- Liangqi Yuan
- Zijie Lei
- Weizhi Zhang
- Kunlun Zhu
- Haodong Yue
- Keyang Xuan
affiliations:
- University of Illinois Urbana-Champaign
- University of Maryland, College Park
- Nanyang Technological University
- Purdue University
- University of Illinois Chicago
arxiv_id: '2608.06867'
url: https://arxiv.org/abs/2608.06867
pdf_url: https://arxiv.org/pdf/2608.06867
published: '2026-08-06'
collected: '2026-08-14'
category: LLM
direction: LLM部署优化 · 模型路由统一基础设施
tags:
- LLM Routing
- Benchmark
- Infrastructure
- Model Selection
- Cost Optimization
one_liner: 提出统一LLM路由抽象、多场景基准xRouteBench及模块化开源工具链，支持16+主流路由算法
practical_value: '- 可复用其LLM路由五组件抽象（上下文/模型编码器、打分函数、决策规则、学习信号），快速搭建业务场景下的多LLM路由系统，比如电商智能客服模型路由、推荐系统query意图匹配的模型分发

  - 借鉴其自动标注路由监督信号的流水线：批量跑候选模型在业务query集的表现，自动生成质量+成本标注，无需人工标注路由标签，大幅降低路由模型训练成本

  - 多Agent系统的每个节点（规划、执行、总结）可单独做路由，根据节点功能选最合适的LLM，比统一用大模型成本降30%+的同时性能还提升，适合电商大促多Agent活动策划、智能导购等场景

  - 成本敏感场景优先选轻量单-turn路由（如SVM、kNN路由），比多-turn路由性价比高很多，个性化路由引入用户侧特征可提升8%+的用户满意度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前异构LLM生态下，没有单个模型能在所有query场景和成本约束下达到最优，模型路由是LLM部署降本增效的核心手段，但现有路由算法形式不统一、实现互不兼容、缺乏标准化评估流程，阻碍了算法的公平对比和业务落地。
### 方法关键点
- 将所有LLM路由统一抽象为序列决策过程，拆解为上下文编码器、模型编码器、打分函数、决策规则、学习信号5个通用组件，覆盖单轮、多轮、个性化三类路由范式
- 实现自动监督数据构建流水线：批量调度候选模型处理基准query，自动统计每个请求的质量得分和token成本，生成路由训练所需的标注数据，无需人工介入
- 发布xRouteBench多场景路由基准，覆盖通用LLM任务、记忆增强、多模态、时序、个性化5类场景，共4767个测试样本
- 开源LLMRouter工具库，内置16+主流路由算法，用户仅需实现路由逻辑和损失函数即可新增自定义路由，支持直接部署为OpenAI兼容接口、ComfyUI可视化原型
### 关键结果
- 学习型路由相对最优固定模型基线，性价比提升14.6%；固定选最大模型的方案始终是性价比最低的选择
- 个性化路由在真实用户偏好匹配任务上准确率达83.05%，比非个性化最优路由高3.8个百分点
- 多Agent系统每个节点独立路由，相比统一使用最大模型，平均性能提升5pct，成本最高下降40%
- 成本约束越严格，轻量单轮路由的表现越优于复杂多轮路由，多轮路由无稳定性能增益
### 核心结论
没有通用最优的路由算法，必须根据业务的性能-成本权衡需求选择对应路由策略
