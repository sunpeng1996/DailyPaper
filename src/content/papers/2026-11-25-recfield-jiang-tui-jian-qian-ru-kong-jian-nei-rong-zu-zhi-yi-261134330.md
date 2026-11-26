---
title: 'RecField: Embedding Recommendations into Spatial Movie Organization as Affordances
  for Serendipitous Encounters'
title_zh: RecField：将推荐嵌入空间内容组织界面以提升偶遇式发现
authors:
- Kenta Oku
affiliations:
- Ryukoku University
arxiv_id: '2611.34330'
url: https://arxiv.org/abs/2611.34330
pdf_url: https://arxiv.org/pdf/2611.34330
published: '2026-11-25'
collected: '2026-11-26'
category: RecSys
direction: 推荐系统 · 偶遇式发现 交互设计
tags:
- serendipity
- interactive recommendation
- user interface
- recommendation evaluation
- information organization
one_liner: 提出嵌入空间内容组织场景的推荐范式，验证推荐对偶遇式发现的直接+间接增益
practical_value: '- 可将推荐从「用户主动获取的服务」重构为「用户执行整理收藏、搭建购物清单等任务时的环境提示」，降低推荐的侵入感，适配电商收藏页、内容APP个人整理页等场景

  - 基于用户自建的内容集合（如自定义片单、购物车同类商品）生成带明确属性标签的分维度推荐（如同导演、同品牌、同材质），相比混合推荐更易获得用户信任，还能激发自发探索

  - 推荐效果评估不能仅看直接点击/加购率，需覆盖推荐带来的间接增益：如用户看到推荐后主动搜索相关内容、重新评估已有收藏的价值，本文数据显示这类隐性贡献占比超85%'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统面向偶遇式发现（serendipity）的推荐研究大多聚焦算法优化，忽略了serendipity本质是用户与系统环境交互的产物；现有评估体系仅关注推荐直接转化率，未覆盖推荐对用户自发探索的间接影响，无法真实衡量推荐的长期价值。
### 方法关键点
- 设计RecField空间组织界面，用户可在自由画布上拖拽电影、创建自定义收藏分区，将推荐从核心服务降维为用户整理收藏时的环境可供性提示
- 采用极简透明的推荐逻辑：基于用户自建收藏的共有属性（导演、演员、IP、风格等）生成聚类，每个推荐列表带明确属性标签（如「导演：宫崎骏」），用户可切换不同维度的推荐
- 组间对照实验设计：实验组带推荐功能，对照组无推荐，同时从系统全局感知、单个物品两个维度评估serendipity，通过行为日志区分推荐的直接/间接影响
### 关键结果
实验基于TMDB的1.17万部热门电影，57名受试者参与，核心结论：
1. 全局感知层面两组无显著差异，但实验组的「意外偶遇内容」感知得分高出17%，效应量0.209
2. 单个物品层面，实验组收藏的电影在「激发观看欲」「拓宽偏好」两个指标上得分显著高出11%、21%，p值均<0.05
3. 实验组仅14%的收藏直接来自推荐列表，剩余86%的收藏虽来自搜索/画布操作，其serendipity评分仍显著高于对照组，间接增益远大于直接转化

**最值得记住的结论**：推荐的价值不止于直接点击转化，其作为环境提示激发用户主动探索、重新评估内容的隐性价值，往往是决定用户长期满意度的核心。
