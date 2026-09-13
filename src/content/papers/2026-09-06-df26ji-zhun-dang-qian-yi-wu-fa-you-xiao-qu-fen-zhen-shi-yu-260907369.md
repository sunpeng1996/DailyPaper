---
title: 'DF26: We Cannot Tell Fake From Real Anymore'
title_zh: DF26基准：当前已无法有效区分真实与AI生成单人演讲视频
authors:
- Severyn Shykula
- Andrii Yermakov
- Ivan Samarskyi
- Dmytro Mishkin
- Jan Cech
- Anastasiia Mishchuk
affiliations:
- Ukrainian Catholic University
- Hover Inc., USA
- Faculty of Electrical Engineering, Czech Technical University in Prague
- Institute of Software Systems of the National Academy of Sciences of Ukraine
arxiv_id: '2609.07369'
url: https://arxiv.org/abs/2609.07369
pdf_url: https://arxiv.org/pdf/2609.07369
published: '2026-09-06'
collected: '2026-09-13'
category: Eval
direction: AIGC检测 · 深度伪造评估基准构建
tags:
- Deepfake Detection
- Text-to-Video
- Benchmark
- AIGC Evaluation
- Distribution Shift
one_liner: 推出包含2691条单人演讲类视频的DF26深度伪造检测基准，验证现有检测能力接近随机猜测
practical_value: '- 电商内容风控场景可直接复用DF26的单人演讲类视频构造逻辑，构建适配业务的AIGC短视频检测测试集，验证现有风控模型对新型文生/图生视频的鲁棒性

  - 涉及数字人直播、AI生成商品宣传视频的业务，可参考DF26的分布偏移评估思路，定期更新检测模型的训练/测试分布，避免模型对新型生成器失效

  - 若业务需要自研深度伪造检测能力，可优先在DF26基准上预验证方案有效性，避免在老旧过时基准上刷点导致线上性能虚高'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有深度伪造检测基准多围绕换脸、面部重定向等传统伪造场景构建，无法覆盖当前文生/图生视频模型输出的全场景伪造内容，尤其单人公开演讲这类高风险场景的检测评估存在空白，现有检测方案对新型生成器泛化性极差。
### 方法关键点
构建DF26开源基准，覆盖单人对镜录制、官方声明、演播室访谈三类公开演讲场景，包含271条真实视频、2420条由7款2025-2026年最新闭源/开源文生/图生视频模型生成的伪造视频，已开放在Hugging Face。
### 关键结果
人类识别DF26中伪造视频的准确率接近随机水平，SOTA深度伪造检测模型的检测性能也接近随机猜测，证明现有评估协议存在严重缺陷，亟需适配新型生成模型分布偏移的专用基准。
