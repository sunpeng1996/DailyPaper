---
title: 'Beyond Preference Following: Benchmarking Profile-Query Arbitration in Personalized
  Text Transformation'
title_zh: 超越偏好跟随：个性化文本转换中画像-查询冲突仲裁基准
authors:
- Tenghao Ji
- Qichen Sun
- Zhuoran Lu
affiliations:
- Independent Researcher
- Peking University
- Center for Advanced AI, Accenture
arxiv_id: '2610.39550'
url: https://arxiv.org/abs/2610.39550
pdf_url: https://arxiv.org/pdf/2610.39550
published: '2026-10-29'
collected: '2026-10-31'
category: Eval
direction: LLM个性化文本生成效果评估
tags:
- Personalized Generation
- LLM Evaluation
- Conflict Arbitration
- Benchmark
- Text Rewrite
one_liner: 发布含64个改写任务、256组任务-偏好对的PCA-Bench，评估LLM的画像与请求冲突仲裁能力
practical_value: '- 搭建电商个性化文案生成、客服Agent时，不能仅以历史偏好跟随率为核心指标，需设计偏好与当前任务请求的冲突仲裁逻辑，避免为贴合历史偏好降低当前任务效果

  - 个性化生成系统的效果评估可复用PCA-Bench的三维评估框架：请求满足度、目标达成度、偏好跟随率，避免单一指标带来的评估偏差

  - 电商场景的个性化改写任务（如营销话术、商品描述定制）可参考基准的冲突类型划分，针对不同冲突等级配置优先级策略，优先保障当前任务诉求'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
基于LLM的个性化写作助手依赖用户历史画像的持久偏好实现定制化生成，但历史偏好常与当前用户的即时请求存在冲突，现有评估仅关注偏好跟随率或请求满足度单一指标，无法衡量冲突场景下的生成质量。
### 方法关键点
构建PCA-Bench评估基准，包含64个通用文本改写任务，针对每个固定文本与请求配置不同的用户画像偏好，共生成256组任务-偏好对，覆盖偏好与请求的全量关系类型；设计三维评估维度：响应规则符合度、请求目标达成度、历史偏好跟随率。
### 关键结果
在3款主流LLM上测试发现：偏好与任务目标冲突时，同时满足规则与偏好的成功率越高，反而可能比无画像生成的质量损失更大；相似的偏好跟随率，在冲突场景下的即时请求满足能力可能存在显著差异。
