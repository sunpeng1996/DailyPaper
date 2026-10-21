---
title: 'SPAR: Stepwise Personalized Autoregressive Recommendation with Prefix-Balanced
  Semantic IDs'
title_zh: SPAR：基于前缀平衡语义ID的分步个性化自回归推荐框架
authors:
- Chunrui Zhang
- Gaoyun Lin
- Chang Zhou
- Zheng Hu
- Qiran Song
- Shimin Cai
- Tao Zhou
affiliations:
- 电子科技大学
- 中国科学技术大学
- 阿里巴巴虎景数字媒体娱乐集团
- 西南交通大学
arxiv_id: '2610.27898'
url: https://arxiv.org/abs/2610.27898
pdf_url: https://arxiv.org/pdf/2610.27898
published: '2026-10-20'
collected: '2026-10-21'
category: GenRec
direction: 生成式推荐 · Semantic ID 自回归优化
tags:
- Generative Recommendation
- Semantic ID
- Autoregressive Decoding
- Personalized Recommendation
- Industrial RecSys
one_liner: 提出融合前缀平衡Semantic ID与分步个性化解码的工业级生成式推荐框架SPAR
practical_value: '- 语义ID构建可复用RQ-PIB方法：按同前缀下的历史交互负载做局部分支平衡，仅以最小语义失真代价就能缓解热门路径马太效应，无需做破坏语义结构的全局平衡

  - 生成式推荐解码可借鉴PATH Decoder设计：分层级压缩长期行为记忆，每步解码根据当前前缀动态检索对应粒度的用户兴趣，结合实时上下文、用户画像提升分支选择准确率

  - 训练策略可复用SFT+DPO的偏好对齐流程：先用历史交互做SFT，再用冻结排序模型给beam search候选打分构造DPO偏好对，进一步提升TOP位推荐准确率

  - 工程落地可参考其模型规模选型结论：1.7B参数的Qwen3在视频推荐场景下达到性价比最优，适配工业级部署的资源约束'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于Semantic ID（SID）的生成式推荐存在两个核心痛点：一是自回归解码每步的前缀对应不同候选集，固定用户表征无法适配从粗到细的兴趣粒度需求，易出现不可逆的分支选择错误；二是同前缀下的历史交互负载高度不平衡，热门路径占比过高放大马太效应，压制小众但匹配用户兴趣的内容露出。
### 方法关键点
- **RQ-PIB前缀平衡SID构建**：先通过残差量化得到初始语义codebook，再按同父前缀下的分支交互负载设置上限，以最小语义失真为代价迁移过载分支下的item，实现局部负载平衡，不破坏全局语义结构。
- **PATH Decoder分步个性化解码**：将长期用户行为按SID层级构建粗到细的多视角记忆，用Q-Former压缩为记忆库；每步解码根据当前生成的前缀，通过交叉注意力动态检索对应粒度的长期兴趣，融合短期行为、用户画像、请求上下文预测下一个SID token。
- **SFT+DPO混合训练**：先以历史交互做监督微调，再用冻结排序模型给beam search候选打分构造正负偏好对，做DPO偏好对齐，进一步提升TOP位推荐准确率。
### 关键实验
在优酷工业级视频推荐数据集上，对比GRU4Rec、SASRec、TIGER、OneRec等基线，离线HR@10/20/50/100平均相对提升2.66%；目标前缀保留率平均提升5.79pp，同前缀下最大分支流量占比平均降低32.84%；7天线上A/B测试（10%流量），用户平均观看时长提升3.95%，播放转化率提升3.38%。
### 核心结论
生成式推荐中Semantic ID的结构设计和个性化解码逻辑必须协同优化，局部前缀维度的分支平衡比全局codebook平衡对生成效果的影响更大。
