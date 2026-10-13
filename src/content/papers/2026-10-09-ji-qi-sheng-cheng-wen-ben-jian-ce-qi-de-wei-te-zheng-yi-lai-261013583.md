---
title: Measuring Artifact Reliance in Machine-Generated Text Detectors
title_zh: 机器生成文本检测器的伪特征依赖度量化研究
authors:
- Anastasia Voznyuk
- Andrey Grabovoy
affiliations:
- Advacheck OÜ
- Moscow State University
arxiv_id: '2610.13583'
url: https://arxiv.org/abs/2610.13583
pdf_url: https://arxiv.org/pdf/2610.13583
published: '2026-10-09'
collected: '2026-10-13'
category: Eval
direction: LLM 生成文本检测性能评估
tags:
- LLM-generated text detection
- artifact reliance
- counterfactual evaluation
- format normalization
- out-of-domain generalization
one_liner: 发现机器生成文本检测器依赖PDF格式伪影，提出格式反事实评估法与预处理优化方案
practical_value: '- 做电商商品文案、用户评论、种草内容的AI生成合规检测时，先对输入文本做格式归一化（统一换行、段落格式），避免模型依赖格式伪特征导致上线后漏判/误判

  - 评估自建的检测类模型（如虚假评论识别、生成文案合规校验）时，可复用格式反事实方法：仅修改文本格式不改动内容，验证模型是否依赖伪特征，筛选鲁棒性高的模型

  - 训练检测类模型时，提前对训练集做格式归一化预处理，可降低跨域泛化gap，显著提升out-of-domain场景的效果'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有机器生成文本检测器在科学文献基准上表现接近完美，但其高准确率是否依赖数据集构建引入的伪特征尚不明确，导致检测器实际落地时鲁棒性存疑。
### 方法关键点
1. 测试6个来源的10个科学文档子集，用仅包含27个表层特征的逻辑回归与现有主流检测器做效果对比，定位核心伪特征为PDF提取的换行格式差异；
2. 提出格式反事实评估方案：仅重排文本换行、不修改任何内容，验证检测器对格式伪影的依赖度；
3. 提出训练前统一做格式归一化的优化方案，消除格式伪特征干扰。
### 关键结果数字
- 仅用4个格式特征即可实现0.996 AUC的分类效果，arXiv子集上表层特征逻辑回归F1达0.951-0.997，超过所有被测检测器；
- 格式反事实操作可让公有检测器20-27%的正确判断发生反转；
- 格式归一化将模型泛化gap从0.32降至0.22，跨域macro-F1从0.33提升至0.65。
