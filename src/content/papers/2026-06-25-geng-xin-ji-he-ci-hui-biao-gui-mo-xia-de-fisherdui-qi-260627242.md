---
title: 'The Geometry of Updates: Fisher Alignment at Vocabulary Scale'
title_zh: 更新几何：词汇表规模下的Fisher对齐
authors:
- John Sweeney
affiliations:
- Sideplane AI
arxiv_id: '2606.27242'
url: https://arxiv.org/abs/2606.27242
pdf_url: https://arxiv.org/pdf/2606.27242
published: '2026-06-25'
collected: '2026-06-27'
category: LLM
direction: LLM迁移学习 · Fisher对齐与轻量任务签名
tags:
- Fisher Alignment
- Transfer Learning
- LLM
- Task Signature
- Training-free
- LoRA
one_liner: 提出FisherSketch，以16KB任务签名实现词汇表规模免训练头Fisher对齐与源选择
practical_value: '- 电商多细分品类/场景的LLM推荐、文案生成LoRA微调源选择：复用FisherSketch思路为每个候选域生成16KB级任务签名，免训练快速排序迁移源，大幅减少全量微调试错的算力成本

  - 针对表征相似性失效场景（如同商品上下文但不同转化目标、同prompt前缀但不同标签分类），不要仅依赖CKA类表征相似度，需结合误差几何信号判断迁移兼容性，避免负迁移

  - 轻量任务签名可落地到推荐多任务路由、持续学习管线：将任务更新几何压缩为极小元数据，快速判断新任务与存量任务的兼容性，辅助任务分组与灾难性遗忘防控'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
共享词表LLM的免训练源选择在科学序列、多任务NLP等场景需求迫切，但存在两大核心痛点：一是CKA、RSA等仅基于激活的表征相似性指标，在「激活暗区」（激活相近但标签条件误差方向差异大）完全失效，无法准确判断迁移兼容性；二是传统Fisher对齐等更新几何指标需实例化K²规模的误差二阶矩，在1e5级词表下单任务存储高达几十GiB，计算与存储成本均不可行。
### 方法关键点
- 理论证明表征-only指标的非可辨识性：存在激活完全相同但头层Fisher对齐为0（参数更新正交）的任务对，仅靠激活表征无法唯一确定迁移效果
- 推导头Fisher对齐的乘积核形式：等价于联合(激活,误差)空间核均值嵌入的余弦相似度，可分解为激活几何、误差几何、耦合项三个独立因子
- 提出FisherSketch流式估计算法：通过分解式Random Maclaurin随机特征+SRHT结构化投影，单遍流式计算联合嵌入，无需实例化K²规模的Fisher矩阵
- 极致存储效率：单任务签名仅16KB（m=4096，float32），流式计算状态仅192KB，可随模型哈希存储，便携性极强
### 关键结果
- 自然域偏移（Llama-3.1-8B，100个共享词表域，24个候选源）：FisherSketch Top-1源选择准确率45.7%±5.0，达到98.44%±0.30的oracle归一化迁移效果，与激活-only基线性能相当
- Verbalizer shift压力测试（固定prompt前缀，激活完全相同）：激活-only基线降至随机水平（20% Top-1），FisherSketch仍达66.7% Top-1、95.7%的oracle归一化迁移效果
- 分子SMILES域验证：FisherSketch与跨域困惑度下降的Spearman相关系数ρ=0.53（p=0.006），激活-only相似性无统计显著性（p=0.081）
### 核心洞见
表征相似性只反映模型的输入表示，而更新几何才真正决定迁移效果，激活暗区下误差几何信号是迁移判断的必要补充
