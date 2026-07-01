---
title: 'DataEvolver: Self-Evolving Multi-Agent Data Construction for Text-Rich Image
  Generation'
title_zh: DataEvolver：面向富文本图像生成的自演进多Agent数据构建框架
authors:
- Siyu Yan
- Yizhen Gao
- Yilin Wang
- Dongxing Mao
- Alex Jinpeng Wang
affiliations:
- Central South University
- The Hong Kong University of Science and Technology
arxiv_id: '2606.31537'
url: https://arxiv.org/abs/2606.31537
pdf_url: https://arxiv.org/pdf/2606.31537
published: '2026-06-29'
collected: '2026-07-01'
category: MultiAgent
direction: 多智体协作 · 数据构建闭环优化
tags:
- Multi-Agent
- Data Construction
- Text-Rich Image Generation
- Self-Evolving
- Feedback Loop
one_liner: 提出四Agent闭环自演进数据构建框架，复用被拒样本反馈提升富文本图像生成质量
practical_value: '- 可直接复用四Agent（检索-校验-复盘-生成）闭环架构做业务数据治理，比如电商商品素材库、广告创意库的自动筛选与补全，将低质样本拒因转化为检索/生成的优化方向，避免重复踩坑

  - 校验-语义复盘的设计可迁移到推荐/广告的物料准入流程，把驳回的低质广告、违规素材的拒因做LLM语义聚合，自动迭代准入规则，还能定向生成长尾品类的优质物料填补覆盖缺口

  - 小模型Agent选型经验可参考：用4B量级小模型即可完成反馈聚合、查询生成、prompt优化等任务，成本低效果够用，替换为更大模型可进一步提升反馈质量

  - 长尾覆盖思路可复用在推荐召回场景：针对召回不足的长尾类目/query，用类似Critic的模块定位覆盖缺口，再定向生成训练样本，提升长尾场景的效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统富文本图像数据构建采用静态爬取-过滤-冻结范式，筛选后的被拒样本直接丢弃，浪费了其中蕴含的OCR错误、语义不匹配、布局异常等失败信号，导致后续数据构建重复出现同类问题，下游富文本图像生成模型的文本渲染效果提升长期受限于训练数据的质量与覆盖度。

### 方法关键点
- 四Agent闭环架构：`Retriever`根据当前策略生成结构化检索查询获取候选样本，`Verifier`做多维度质量校验输出通过样本+细粒度拒因统计，`Critic`将轮次反馈聚合为自然语言语义指导，更新下一轮的检索、生成策略，`Generator`针对覆盖缺口做定向合成补全长尾区域
- 反馈驱动无参数迭代：每轮的通过/拒因数据存入经验库，仅在自然语言策略空间更新检索查询、生成prompt，无需调整任何模型参数，迭代成本极低
- 多维度校验体系：Verifier同时评估感知图像质量、OCR识别质量、语义一致性三个维度，拒因细分为重复、模糊、OCR失败、语义不匹配、布局损坏等类别，为策略优化提供精准信号

### 关键实验
基于PixArt-α、Show-o2两个下游生成模型验证，在0.75M规模匹配数据量下，对比MARIO、AnyWord两个SOTA基线：PixArt-α上OCR-F1在TextScenesHQ提升85.3%、在LongTextBench提升35.3%；Show-o2上对应提升136.8%、62.9%，效果不绑定特定下游模型。消融实验显示去掉Critic模块OCR-F1最多下降43%，去掉Generator模块最多下降21%，验证两个核心模块的必要性。同时构建的数据集类目覆盖度比基线高6~18pct，长尾覆盖提升0.7~1.8pct。

### 核心结论
数据构建不是一次性的静态预处理步骤，而是可以通过反馈闭环持续迭代的自适应过程，被丢弃的低质样本里藏着最有效的优化方向。
