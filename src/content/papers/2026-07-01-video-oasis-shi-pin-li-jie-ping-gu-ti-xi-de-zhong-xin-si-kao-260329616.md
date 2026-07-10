---
title: 'Video-Oasis: Rethinking Evaluation of Video Understanding'
title_zh: Video-Oasis：视频理解评估体系的重新思考
authors:
- Geuntaek Lim
- Sungjune Park
- Jaeyun Lee
- Inwoong Lee
- Taeoh Kim
- Dongyoon Wee
- Minho Shim
- Yukyung Choi
affiliations:
- Sejong University, South Korea
- NAVER Cloud, South Korea
arxiv_id: '2603.29616'
url: https://arxiv.org/abs/2603.29616
pdf_url: https://arxiv.org/pdf/2603.29616
published: '2026-07-01'
collected: '2026-07-10'
category: Eval
direction: 多模态大模型 · 视频理解基准评估
tags:
- Video-LLM
- Benchmark
- Multimodal Evaluation
- Video Understanding
- Diagnostic Suite
one_liner: 推出Video-Oasis诊断套件，系统审计现有视频理解基准，筛选剔除无视觉依赖的捷径样本
practical_value: '- 做短视频/直播相关的多模态推荐评估时，可复用该套件的捷径样本筛查逻辑，剔除无需看视频就能答对的测试用例，避免高估模型性能

  - 搭建自有业务多模态评测集时，可参考其评估标准，优先保留依赖视觉输入与时序上下文的样本，提升评测集的业务相关性

  - 选型Video-LLM用于短视频内容理解、商品视频打标等场景时，用提纯后的视频原生测试集验证，更能选出实际表现好的模型'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前Video-LLM基准无法区分性能来自视觉感知、语言推理还是知识先验，行业缺乏统一的视频理解评估标准，大量现有benchmark存在捷径样本干扰评估准确性。
### 方法关键点
推出Video-Oasis可持续诊断套件，通过两类测试筛查捷径样本：一是无视觉输入仅提供问题，二是提供视觉输入但移除时序上下文；最终提纯出仅依赖视频视觉与时序信息的原生挑战测试集，可用于验证不同算法设计对鲁棒视频理解的贡献。
### 关键结果
审计发现现有视频理解基准中55%的样本无需视觉输入或时序上下文即可解答；剔除捷径样本后，SOTA Video-LLM的表现仅略高于随机猜测，暴露现有模型的真实视频理解能力存在显著短板。
