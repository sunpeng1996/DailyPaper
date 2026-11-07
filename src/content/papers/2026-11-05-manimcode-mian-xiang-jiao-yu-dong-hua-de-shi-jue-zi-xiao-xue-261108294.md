---
title: 'ManimCode: Learning Visual Self-Correction for Educational Animation'
title_zh: ManimCode：面向教育动画的视觉自校正学习框架
authors:
- Zhengyang Liang
- Lizi Liao
affiliations:
- Singapore Management University
arxiv_id: '2611.08294'
url: https://arxiv.org/abs/2611.08294
pdf_url: https://arxiv.org/pdf/2611.08294
published: '2026-11-05'
collected: '2026-11-07'
category: Agent
direction: 自校正Agent · 代码生成优化
tags:
- LLM Agent
- Self-Correction
- Code Generation
- SFT
- Reinforcement Learning
- Dataset Construction
one_liner: 构建含完整修正轨迹的Manim数据集，训练4B单模型实现教育动画代码的自主编写审核与修正
practical_value: '- 自校正Agent训练范式可直接复用：先通过带完整修正轨迹的role-conditioned SFT让单模型同时承担生成、审核、修正三类角色，再用RL优化分布外错误的修复效果，适配电商文案生成、商品短视频脚本生成等需反复调优的生成类业务

  - 高质量轨迹数据构建方法可借鉴：采用「生成-执行-审核-修正」的引导式流水线，结合RAG引入API文档约束，可低成本批量生产带中间过程的标注数据，解决业务场景中修正轨迹数据稀缺的问题

  - 小模型落地技巧可参考：单4B模型即可替代多个大模型完成全链路自校正任务，无需多模型调度，大幅降低推理部署成本，适合端侧或资源受限的业务场景'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
Manim实现程序化教育动画生成时，即使渲染成功仍可能存在视觉缺陷、内容错误、解释缺失等问题，现有自校正Agent方案高度依赖闭源大模型，且公开数据集普遍缺少完整的反馈-修正轨迹，无法支撑小模型自校正能力的训练。
### 方法关键点
1. 搭建渲染引导的数据集流水线，结合API文档RAG迭代完成Manim代码的生成、执行、审核、修正，构建含24034条渲染验证、质量过滤记录的ManimData，留存全链路中间状态与修正轨迹；
2. 基于角色条件SFT训练单4B模型ManimCode，同时具备代码编写、视觉审核、错误修正能力；
3. 针对分布外错误，基于渲染结果和无参考质量反馈对修正模块做RL优化，提升泛化性。
### 关键结果
在ManimData-test、ManimBench上渲染成功率分别达96.6%、97.0%，较同规格未训练4B模型提升44pct、15pct，视频质量分分别提升0.46、0.44；集成到两套长视频生成系统后，完成率分别从16.2%、22.2%提升至91.5%、100%，教育效果与视觉质量同步提升。
