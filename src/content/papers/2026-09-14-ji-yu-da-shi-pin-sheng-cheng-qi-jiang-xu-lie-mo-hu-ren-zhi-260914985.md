---
title: Converting Sequenced Fuzzy Cognitive Maps to Causal Virtual Worlds with Large
  Video Generators
title_zh: 基于大视频生成器将序列模糊认知图转换为因果虚拟世界
authors:
- Akash Kumar Panda
- Olaoluwa Adigun
- Bart Kosko
arxiv_id: '2609.14985'
url: https://arxiv.org/abs/2609.14985
pdf_url: https://arxiv.org/pdf/2609.14985
published: '2026-09-14'
collected: '2026-09-16'
category: Agent
direction: Agent · 可控因果虚拟内容生成
tags:
- Fuzzy Cognitive Map
- LLM Agent
- Video Generation
- Causal Modeling
- Virtual World
one_liner: 结合模糊认知图、LLM与大视频生成Agent，实现具备可控因果逻辑的虚拟世界视频生成
practical_value: '- 电商虚拟营销内容（商品演示、短剧）生成可借鉴FCM因果建模思路，先定义实体交互规则再生成内容，避免逻辑混乱

  - Agent驱动的多模态内容生成可复用「因果规则提取→LLM写脚本→多模态生成器输出」pipeline，提升内容可控性

  - 推荐系统的用户/内容交互因果建模可参考FCM的反馈动态平衡逻辑，提升因果推断准确性'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有大视频生成模型缺乏可控因果逻辑约束，生成内容易出现逻辑冲突，无法满足需连贯因果叙事的场景需求。

### 方法关键点
1. 用反馈模糊认知图（FCM）建模虚拟世界细粒度因果结构，局部支持模糊/部分因果规则，通过反馈结构生成全局平衡态定义因果场景；
2. 提取「如果A则B」形式的动态元规则，A为用户/Agent可控的因果扰动输入，FCM瞬态反馈动态定义因果关联，B为最终平衡吸引子（如极限环、不动点）；
3. LLM Agent基于元规则序列生成脚本，大视频生成器按照动态流输出对应视频场景。

### 关键结果
基于5节点海洋FCM模型，用Gemini 3.1生成脚本、Veo 3.1生成1分钟海豚鲨鱼主题因果连贯的虚拟世界视频，方案可扩展到更大规模FCM实现更复杂沉浸式内容。
