---
title: LLMs Are Already Confidence-Aware Zero-Shot Classifiers
title_zh: 大语言模型本身就是具备置信度感知能力的零样本分类器
authors:
- Owen Cook
- Xingyi Song
affiliations:
- University of Sheffield
arxiv_id: '2611.25289'
url: https://arxiv.org/abs/2611.25289
pdf_url: https://arxiv.org/pdf/2611.25289
published: '2026-11-18'
collected: '2026-11-20'
category: LLM
direction: LLM零样本分类 · 置信度提取优化
tags:
- Zero-Shot Classification
- Confidence Calibration
- Constrained Decoding
- Logit Scoring
- Open-source LLM
one_liner: 系统对比LLM零样本分类的多种置信度提取方法，提出决策点打分法降88%-96%解码步骤，验证开源模型媲美商用分类器
practical_value: '- 电商评论分类、用户意图识别等零样本分类场景优先选择logit-based置信度方法，AUROC比黑盒口头置信度高17~20个点，错误预测识别能力显著更强

  - 多标签分类（如77类/151类电商意图识别）可复用决策点仅打分法，最高降低96%解码步骤，不损失分类效果，适配高吞吐在线分类需求

  - 极致低延迟要求的分类场景（如实时搜索query分类）可将标签映射为单token，AUROC几乎不降，仅损失3~6个点准确率，大幅提升推理速度

  - 零样本分类选型可优先考虑Qwen 3.5 9B，9B参数量小模型即可达到与商用Jev 1.13.0相当的AUROC效果，推理成本远低于30B+大模型'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
零样本LLM文本分类在数据稀缺、标签迭代频繁的场景（如电商意图识别、评论分类）相比微调分类器成本优势显著，但当前各类置信度提取方法缺乏统一的横向对比，且分类任务的不确定性多来自任务歧义而非知识缺失，现有方法适配性差，置信度结果可靠性不足，亟需明确不同方法的优劣及优化方向。
### 方法关键点
- 覆盖4类置信度提取方案：黑盒方法（口头置信度输出、多采样投票、P(True)后验打分）、白盒logit打分方法（多类标签概率聚合、长度归一化）
- 提出decision-only scoring方法：仅对解码trie上存在多分支的决策节点计算概率，跳过无选择的强制输出token，降低冗余计算
- 测试11个参数量1B~32B的开源LLM，覆盖5个不同标签规模（3~151类）的分类数据集，从分类效果、区分度、校准度三类指标全面评估
### 关键结果
- 置信度提取方法对分类准确率影响极小，logit-based方法平均AUROC达0.74~0.77，远高于黑盒方法的0.57~0.66
- 决策点打分法在Banking77/CLINC150/20NG数据集分别降低96%/92%/88%解码步骤，效果与全标签打分持平
- 标签替换为单token可保留区分度，平均仅损失3~6个准确率点
- 最优开源配置（Gemma 4 31B、Qwen 3.5 9B）效果与商用Jev 1.13.0分类器相当

**最值得记住的结论**：零样本LLM分类优先选logit-based置信度方法远优于口头输出置信度，决策点剪枝可在几乎无损效果的前提下大幅提升推理效率。
