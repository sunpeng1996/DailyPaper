---
title: 'MetaCaster: Meta-Harness-Optimized Agent for End-to-End Few-Shot Learning
  of Lightweight Time Series Forecasters'
title_zh: MetaCaster：元Harness优化Agent实现轻量时间序列预测器端到端少样本学习
authors:
- ChengAo Shen
- Wenchao Yu
- Fangyu Wu
- Dongjin Song
- Hanghang Tong
- Dongsheng Luo
- Wei Cheng
- Haifeng Chen
- Jingchao Ni
affiliations:
- University of Houston
- NEC Labs
- University of Waterloo
- University of Connecticut
- University of Illinois at Urbana-Champaign
arxiv_id: '2608.23473'
url: https://arxiv.org/abs/2608.23473
pdf_url: https://arxiv.org/pdf/2608.23473
published: '2026-08-24'
collected: '2026-08-25'
category: Agent
direction: Agent 轻量时序预测少样本优化
tags:
- Multi-Agent
- Time Series Forecasting
- Few-Shot Learning
- Harness Optimization
- Lightweight Model
one_liner: 提出元Harness优化多Agent框架，仅用少量样本自动训练高性能轻量时序预测器，推理成本远低于时序大模型
practical_value: '- 电商/推荐场景的时序预测（销量、流量、库存预估等）可直接复用该框架，仅用少量历史数据训练轻量预测模型，规避大模型推理成本过高问题

  - Agent Harness优化（而非LLM微调）的思路可迁移到业务Agent开发中，外层优化Agent的系统提示、技能库而非修改LLM参数，适配低成本API切换需求，降低迭代成本

  - 可参考其统一API轻量模型库的设计思路，将常用的排序、预估小模型封装为统一调用接口，配合Agent自动完成模型选择、超参调优，降低人工运维成本

  - 少样本场景下的生成式数据增强不要仅追求数据分布相似度，要对齐下游任务目标，可复用在推荐/广告的少样本样本增强场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前时序预测存在明显痛点：大模型推理成本过高无法落地边缘/低资源场景，轻量预测器效果好但依赖大量训练数据，少样本场景（比如新商品销量预测、新门店流量预测）下易过拟合；传统数据增强仅追求分布一致，无法保证下游预测性能，亟需低成本的少样本轻量模型训练方案。

### 方法关键点
- 采用**Agent-as-Engineer**范式，三个Agent分工：MGAgent根据少样本和文本上下文生成符合领域约束的训练数据；FTAgent调用包含23个SOTA轻量时序预测器的统一库LT-LIB，自动完成训练、超参搜索、最优模型筛选；HPAgent作为元优化器自动优化MGAgent的Harness（系统提示、技能库等），直接对齐数据生成目标与下游预测精度。
- 不对LLM做微调，仅优化Harness参数，优化后的Harness可跨不同LLM迁移，支持灵活切换低成本API。
- 部署阶段仅保留训练好的轻量预测器，无Agent和LLM开销，适配低资源运行环境。

### 关键结果
在18个跨9个领域的时序数据集上对比14个baseline（时序生成模型、传统增强方法、时序大模型等），K=30的少样本场景下，30个测试任务中19个取得最优MSE，性能接近全量数据训练的效果；推理延迟比时序大模型低3个数量级，参数量少5个数量级。

**最值得记住的一句话**：对于可拆分的任务，Agent不需要直接做执行，作为中间「工程师」自动化生成专用轻量模型，既能拿到大模型的知识增益，又能保障推理的极致效率。
