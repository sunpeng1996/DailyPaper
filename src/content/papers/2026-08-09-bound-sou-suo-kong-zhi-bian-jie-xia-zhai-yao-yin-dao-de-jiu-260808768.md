---
title: 'BOUND: Brief-Guided Corrective Preference Distillation at Search-Control Boundaries'
title_zh: BOUND：搜索控制边界下摘要引导的纠偏偏好蒸馏框架
authors:
- Qingying Niu
- Ruiyang Ren
- Wayne Xin Zhao
- Yaliang Li
affiliations:
- Renmin University of China
- Alibaba Group
arxiv_id: '2608.08768'
url: https://arxiv.org/abs/2608.08768
pdf_url: https://arxiv.org/pdf/2608.08768
published: '2026-08-09'
collected: '2026-08-11'
category: Agent
direction: 搜索Agent · 偏好蒸馏纠偏
tags:
- Search Agent
- Preference Distillation
- DPO
- Persistent Search Drift
- RAG
one_liner: 训练侧通过特权摘要引导构造纠偏偏好对，解决搜索Agent持续漂移问题
practical_value: '- 电商搜索Agent训练可复用特权摘要设计：训练侧构造包含原始query、约束、已验证信息、缺失信息、漂移状态的结构化摘要，作为教师端锚定参考，推理侧无需额外输入不增加延迟

  - 偏好对构造trick可迁移：针对学生自身产生的错误轨迹构造同状态正负例对，而非直接模仿教师全轨迹，训练效率更高，更适配学生实际犯错场景

  - 可结合DPO做轻量蒸馏：仅用千级偏好对做1轮DPO训练即可显著提升多步搜索效果，适合小模型端侧搜索Agent快速迭代'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
基于LLM的深度搜索Agent依赖迭代检索+推理完成多步信息查询任务，但局部相关的检索结果容易引发锚点漂移、核心约束丢失、局部主题偏移三类持续漂移问题，现有轨迹SFT、粗粒度RL等方法无法区分任务对齐的决策和局部看似合理、实际会加剧漂移的决策，长交互下信用分配效率极低。

### 方法关键点
- 训练侧构造教师端专属的特权搜索状态摘要，固定保留原始搜索目标、核心约束、已确认证据、缺失信息、漂移状态5个字段，锚定任务对齐标准，避免被已漂移的上下文误导
- 结合摘要引导的实时决策评估和轨迹最终结果，构造两类同状态偏好对：失败轨迹中错误续跑与对应学生专属纠偏续跑的对比、成功轨迹中合理停止回答与不必要继续检索的对比，仅保留通过格式、一致性校验的有效对
- 用DPO将偏好蒸馏到学生模型，训练完成后推理侧仅需常规状态输入，无额外推理开销

### 关键实验
在4个多跳QA、3个深度搜索基准上测试，与同初始化的Trajectory SFT相比，Bamboogle EM提升5.6个点，BrowseComp-Plus准确率提升4.8个点；仅4B参数的BOUND效果超过多数7B参数搜索基线，在BrowseComp-Plus上准确率29.6%、召回32.1%，优于DeepSeek-R1-0528、Search-R1-32B等大模型。

**最值得记住的一句话**：解决搜索Agent漂移不需要增加推理开销，只需在训练侧用特权信息锚定原始需求，针对学生自身的错误做局部偏好蒸馏即可。
