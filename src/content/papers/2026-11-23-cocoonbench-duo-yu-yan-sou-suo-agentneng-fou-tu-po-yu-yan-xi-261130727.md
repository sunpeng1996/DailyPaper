---
title: 'CocoonBench: Can Multilingual Search Agents Escape Language Information Cocoons?'
title_zh: CocoonBench：多语言搜索Agent能否突破语言信息茧房
authors:
- Hongchuan Zeng
- Bowen Liu
- Changjiang Gao
- Senyu Han
- Zhipei Xu
- Peisong Wang
- Xinbing Liang
- Yuhan Li
- Nuo Chen
- Blaze Chen
affiliations:
- 腾讯混元团队
- 南京大学
- 香港城市大学
- 上海交通大学
- 香港科技大学（广州）
arxiv_id: '2611.30727'
url: https://arxiv.org/abs/2611.30727
pdf_url: https://arxiv.org/pdf/2611.30727
published: '2026-11-23'
collected: '2026-11-24'
category: Agent
direction: 多语言搜索Agent评测与能力诊断
tags:
- MultilingualAgent
- SearchAgent
- Benchmark
- CrossLingualRetrieval
- FailureDiagnosis
one_liner: 推出首个强制跨语言证据聚合的多语言搜索Agent评测基准及路径对齐诊断框架
practical_value: '- 跨境多语言电商搜索/商品推荐Agent开发中，可基于实体多语言覆盖度设计路由策略，避免进入无效语言分支浪费算力，不要仅依赖简单语言切换逻辑

  - 可复用路径对齐失败诊断框架，拆解Agent搜索全链路问题，快速定位是语言路由错误、证据链拼接错误还是答案利用错误，加速系统迭代

  - 构建多语言任务评测集时，可借鉴基于Wikidata的最小语言覆盖校验法，确保任务必须跨语言才能解决，避免出现单语言即可完成的评测作弊点'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多语言搜索Agent评测多仅修改提示或证据的语言，未强制要求跨语言聚合证据，无法衡量Agent是否会陷入仅用单一语言搜索、错过其他语言有效信息的「语言信息茧房」问题，跨境电商、多语言内容推荐等场景的Agent能力缺乏针对性评测标准。

### 方法关键点
- 基于Wikidata知识图谱挖掘答案唯一、每条线索均必要的多跳任务，校验任务的最小语言覆盖≥2，确保必须跨至少2种语言才能获取所有实体线索
- 每个任务生成中文、英文、任务专属指定语言（DL）三个平行提示，保留相同语义和证据结构
- 配套路径对齐的失败诊断机制，将错误分为3大类：语言覆盖不全（L）、证据路径恢复失败（T）、看到答案仍未正确输出（R）

### 关键实验
在200个跨语言多跳任务上测试10个SOTA模型，平均准确率最高仅69.7%（Claude-Opus-4.8），最低为33.8%（DeepSeek-V4-Flash）；65.7%的错误来自未覆盖全部所需语言，其中仅5.8%是完全不切换语言，32.3%的错误是覆盖所有需要语言后仍未拼接出有效证据链。

### 核心结论
多语言模型本身的理解生成能力，不等于多语言搜索的路由与证据聚合能力，突破语言信息茧房需要主动规划语言访问路径，而非被动切换语言。
