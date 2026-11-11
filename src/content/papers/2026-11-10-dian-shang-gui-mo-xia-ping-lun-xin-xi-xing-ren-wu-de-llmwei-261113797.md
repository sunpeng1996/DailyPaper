---
title: Auditing LLM Pseudo-Label Distillation for Review Informativeness at E-Commerce
  Scale
title_zh: 电商规模下评论信息性任务的LLM伪标签蒸馏方案审计
authors:
- M. Emin Dogan
- Cansu Er
- Aysenur Kulunk
- M. Furkan Eseoglu
- H. Bahadir Sahin
affiliations:
- Hepsiburada
arxiv_id: '2611.13797'
url: https://arxiv.org/abs/2611.13797
pdf_url: https://arxiv.org/pdf/2611.13797
published: '2026-11-10'
collected: '2026-11-11'
category: RecSys
direction: 电商评论处理 · LLM伪标签蒸馏
tags:
- LLM-Distillation
- Pseudo-Labeling
- Review-Ranking
- E-Commerce
- Weak-Supervision
one_liner: 审计电商评论信息性任务的LLM伪标签蒸馏的泛化性、对齐度与吞吐量
practical_value: '- 做UGC标签蒸馏时，不能仅以和教师LLM的一致性为唯一评估指标，必须补充小批量业务场景人工标注校验，避免时序/新SKU场景下对齐度下降

  - 小语种本地电商评论处理优先选领域预训练单语种encoder，跨市场跨语言场景优先选XLM-R，可平衡效果与推理成本

  - 蒸馏得到的小encoder在单L4上推理速度是Gemini 3.1 Flash-Lite的50.2倍，可直接落地百万级评论离线批量打标、实时评论排序场景

  - 输入增强策略（如加品类前缀）的效果高度依赖目标场景，不要盲目复用，必须在业务对应测试集上做验证'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商场景下需要快速识别高信息性评论辅助用户决策，直接调用大模型打标成本高、时延高，LLM伪标签蒸馏小encoder是常用落地方案，但过往方案大多只评估和教师模型的一致性，缺乏和人工标注规则的对齐校验，也未验证新SKU、时序偏移等真实业务场景的泛化性，存在落地风险。

### 方法关键点
- 数据：覆盖534万土耳其电商评论，按SKU拆分训练/验证/IID测试集，另设严格新SKU时序OOT测试集，邀请1名领域专家标注4万条评论做人工对齐校验
- 教师模型：冻结Gemini 3.1 Flash-Lite，输入评论+商品名+品类，输出3档硬伪标签（0无产品证据/1有限相关属性/2明确可参考证据）
- 学生模型：对比BERTurk、XLM-R、ModernBERT等encoder，交叉测试CE、CORN序数回归损失，以及是否添加H3品类前缀的输入增强方案
- 评估维度：教师保真度（和Gemini标签一致性）、人工对齐度（和专家标注一致性）、推理吞吐量、跨市场泛化性

### 关键结果
- 全量新SKU OOT集上，加H3品类前缀可让BERTurk的QWK提升0.0016~0.0023，ModernBERT+CORN+H3前缀的教师保真度最高，QWK达0.9223
- 1.6万时序OOT标注子集上，加H3品类前缀反而让CORN损失的QWK下降0.004，和人工标注的对齐度同步下降
- 单L4 GPU上，学生BERTurk推理速度达2218条/秒，是Gemini教师pipeline速度的50.2倍
- 跨亚马逊数据集测试时，XLM-R的跨语言跨市场教师保真度最高，QWK达0.7614，优于单语种预训练模型

### 核心结论
仅教师保真度不足以建立和业务编辑规则的对齐，蒸馏方案必须针对目标场景做独立人工标注校验。
