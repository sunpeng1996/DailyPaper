---
title: MARS Technical Report
title_zh: MARS：多阶段智能体驱动的个性化推荐管线编排系统
authors:
- Tong Liu
- Chaoqun Hou
- Longxiang Xiong
- Junhong Lou
- Jiaqi Zheng
- Qixin Li
- Zixin Zhao
- Yong Duan
- Xiannian Hu
- Fengze Jiang
affiliations:
- Taobao
arxiv_id: '2611.24006'
url: https://arxiv.org/abs/2611.24006
pdf_url: https://arxiv.org/pdf/2611.24006
published: '2026-11-18'
collected: '2026-11-19'
category: Agent
direction: Agent 推荐全链路编排优化
tags:
- Agent4Rec
- Pipeline Orchestration
- LLM Fine-tuning
- RL for RecSys
- Production Deployment
one_liner: 用轻量微调Qwen3-0.6B近线Agent实现推荐全链路用户级动态编排，淘宝场景GMV最高提7.34%
practical_value: '- 可直接复用近线Agent+缓存的管线编排架构：异步生成用户级配置，完全不占用在线关键路径，搭配schema校验、默认配置降级、全局Kill开关三重保障，上线风险极低，适合工业级推荐/广告系统快速落地

  - 小参数LLM结构化决策训练范式可迁移：先大模型蒸馏SFT保证输出格式合规，再通过ActionMask的偏好优化聚焦动作差异信号，最后用沙箱重放+冻结奖励模型做RL迭代，全程无需探量放流即可完成策略优化，避免业务损失

  - 推荐领域prompt注入方法可直接套用：将系统默认参数、合法范围、用户分群调优经验转化为自然语言写入系统prompt，实验显示该操作可避免10%+的业务指标下跌，是低投入高收益的优化手段'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业级推荐系统普遍采用多阶段级联架构，但召回通道配额、模型选择、分数融合等管线级配置均为全局静态人工调优，无法适配不同用户的意图、价格敏感度、行为模式差异，且配置组合空间过大无法手动枚举，直接在线A/B探索成本高、风险大，缺乏有效的反事实反馈训练信号。
### 方法关键点
- 架构解耦近线生成与在线执行：采用微调的Qwen3-0.6B作为近线Agent，异步生成7维结构化用户级配置（含管线模式、召回通道配额、排序模型选择、融合权重、重排设置等），校验后写入iGraph缓存，在线服务直接读取缓存，完全不引入LLM推理延迟，搭配schema校验、incumbent降级、全局Kill开关保障服务稳定性。
- 三阶段后训练范式：① 置信度感知SFT：用Qwen3.6-Max作为教师蒸馏，将输出格式合规率从1%提升至99.8%，再通过Wilson下界筛选经过执行验证的正样本对齐业务效率；② FAPO偏好优化：采用ActionMask仅对比配置差异部分的token，避免格式token稀释训练信号，搭配历史V2P后验权重提升偏好的业务适配性；③ GRPO：基于请求快照在沙箱重放执行候选配置，用冻结的CTR/CVR奖励模型打分，无需放流即可完成在线策略迭代。
### 关键结果
在淘宝5个营销场景千万级DAU下开展两周A/B测试，对比基线生产系统，最高V2P提升5.22%，GMV提升7.34%，CTR实现正向提升，在线服务平均latency降低12ms，约20%的请求被路由至极简管线模式，有效降低计算成本。

最值得记住的一句话：推荐系统的个性化可从单阶段的item打分延伸到全管线的动态编排，轻量Agent异步决策+缓存的架构完全可在不影响在线性能的前提下拿到显著业务增益。
